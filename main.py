import socket
import struct
import sys

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
        self.server_socket.bind((self.host, self.port))
        print(f"server is listening on {self.host}:{self.port}")

    def unpack_data(self,data):
        message = Message()
        message.version, message.message_type, message.token_length, message.code = struct.unpack('!HHLQ', data[:16])
        message.message_id = struct.unpack('!16s', data[16:32])[0]
        message.token = struct.unpack(f'!{message.token_length}', data[32:message.token_length])
        message.options = struct.unpack('!32', data[64:96])
        message.payload = data[96:]

        return message

    def handle_request(self, data, client_address):
        message = self.unpack_data(data)

        if message.code == 1:  # GET
            print(f"Received CoAP GET request from {client_address}")
            response_payload = "Hello, client!"
            response = struct.pack(f'!BBBHQ{len(message.token)}s{len(response_payload)}s',
                                   message.version, 2, 0, 205, message.message_id, message.token,
                                   response_payload.encode('utf-8'))
            self.server_socket.sendto(response, client_address)
        elif message.code == 2:  # POST
            print(f"Received CoAP POST request from {client_address}")
            response_payload = "success"
            response = struct.pack(f'!BBBHQ{len(message.token)}s{len(response_payload)}s',
                                   message.version, 2, 0, 205, message.message_id, message.token,
                                   response_payload.encode('utf-8'))
            self.server_socket.sendto(response, client_address)
        elif message.code == 3:  # PUT
            print(f"Received CoAP PUT request from {client_address}")
            response_payload = "success"
            response = struct.pack(f'!BBBHQ{len(message.token)}s{len(response_payload)}s',
                                   message.version, 2, 0, 205, message.message_id, message.token,
                                   response_payload.encode('utf-8'))
            self.server_socket.sendto(response, client_address)
        elif message.code == 4:  # DELETE
            print(f"Received CoAP DELETE request from {client_address}")
            response_payload = "success"
            response = struct.pack(f'!BBBHQ{len(message.token)}s{len(response_payload)}s',
                                   message.version, 2, 0, 205, message.message_id, message.token,
                                   response_payload.encode('utf-8'))
            self.server_socket.sendto(response, client_address)


    def run(self):
        try:
            while True:
                data, client_address = self.server_socket.recvfrom(1024)
                print(f"Received data from {client_address}: {data.decode('utf-8')}")
                message = Message()
                message = self.unpack_data(data)
                response = "Hello, client!"
                self.server_socket.sendto(response.encode('utf-8'), client_address)
        except KeyboardInterrupt:
            print("Server stopped by the user.")
        finally:
            self.server_socket.close()

class Window(QWidget):
    def __init__(self, parent = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ui = Ui_Form()
        ui.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    server = Server('localhost', 12345)
    server.run()
    app.exec_()
