import socket
import struct

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


    def run(self):
        try:
            while True:
                data, client_address = self.server_socket.recvfrom(1024)
                print(f"Received data from {client_address}: {data.decode('utf-8')}")

                response = "Hello, client!"
                self.server_socket.sendto(response.encode('utf-8'), client_address)
        except KeyboardInterrupt:
            print("Server stopped by the user.")
        finally:
            self.server_socket.close()

if __name__ == "__main__":
    server = Server('localhost', 12345)
    server.run()
