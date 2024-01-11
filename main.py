import socket
import struct
import sys
from actions import *
import threading
from PySide6.QtWidgets import *

from interfaceQt import Ui_Form


class Message:
    def __init__(self):
        self.version = None
        self.message_type = None
        self.token_length = None
        self.code = None
        self.message_id = None
        self.token = None
        self.options = None
        self.payload = None


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        print(f"server is listening on {self.host}:{self.port}")

    def stop(self):
        self.server_socket.close()
        print("Server has been stopped.")
    
    def unpack_data(self,data):
        try:
            message = Message()
            if len(data) < 96:
                raise ValueError("Data packet too short for header")

            header = data[:16]
            if len(header) != 16:
                raise ValueError("Invalid header length")

            message.version, message.message_type, message.token_length, message.code = struct.unpack('!HHLQ', header)
            message.message_id = struct.unpack('!16s', data[16:32])[0]

            token_end = 32 + message.token_length
            message.token = struct.unpack(f'!{message.token_length}s', data[32:token_end])[0]

            options_end = 64 + 32
            message.options = struct.unpack('!32s', data[64:options_end])[0]

            message.payload = data[options_end:]

            return message
        except struct.error as e:
            print(f"Error unpacking data: {e}")
            return None


    def run(self):
        try:
            while True:
                data, client_address = self.server_socket.recvfrom(1024)
                print(f"Received data from {client_address}: {data.decode('utf-8')}")
                self.handle_request(data, client_address)
        except KeyboardInterrupt:
            print("Server stopped by the user.")
        finally:
            self.server_socket.close()


    def handle_request(self, data, client_address):
        message = self.unpack_data(data)
        if message:
            #Payload is a string with format "action;folder_path;file_name;[content]"
            try:
                parts = message.payload.decode('utf-8').split(';')
                action = parts[0]
                folder_path = parts[1]
                file_name = parts[2]
                content = parts[3] if len(parts) > 3 else None

                if action == "create":
                    success = create_empty_file(folder_path, file_name)
                elif action == "delete":
                    success = delete_file(folder_path, file_name)
                elif action == "update":
                    success = update_file(folder_path, file_name, content)
                elif action == "read":
                    file_content = read_file_content(folder_path, file_name)
                    success = file_content is not None

                response_payload = "Success" if success else "Failure"
                if action == "read" and success:
                    response_payload = file_content

                response = struct.pack(f'!BBBHQ{len(message.token)}s{len(response_payload)}s',
                                       message.version, 2, 0, 205, message.message_id, message.token,
                                       response_payload.encode('utf-8'))
                self.server_socket.sendto(response, client_address)

            except IndexError:
                print("Invalid message format received")
            except Exception as e:
                print(f"Error handling request: {e}")
        else:
            print("Invalid message received")

class Window(QWidget):
    def __init__(self, parent = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.server = None
        self.server_thread = None
        self.IP = self.get_ip_address()
        self.show()
        self.ui.button_browse.clicked.connect(self.browseFolder)
        self.ui.input_text_address.setText(self.IP)
        self.ui.button_start.clicked.connect(self.toggleServer)
    
    def browseFolder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.ui.input_text_rootfolder.setText(folder_path)
    
    def get_ip_address(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("100.255.255.255", 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = "127.0.0.1"
        finally:
            s.close()
        return IP
    
    def toggleServer(self):
        if self.ui.button_start.text() == "Start":
            self.server = Server(self.IP, 12345)  
            self.server_thread = threading.Thread(target=self.server.run, daemon=True)
            self.server_thread.start()
            self.ui.button_start.setText("Stop")
        else:
            if self.server:
                self.server.stop()
            self.ui.button_start.setText("Start")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
