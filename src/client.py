import socket
import ssl
import os
import time

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432

class Client:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SSL = False
    
    def send_message(self, message):
        if self.SSL:
            context = ssl.create_default_context()
            # working_dir = os.path.dirname(os.path.abspath(__file__))
            # server_cert = os.path.join(working_dir, 'cert.pem')
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            self.client_socket = context.wrap_socket(self.client_socket, server_hostname=HOST)

        total_data = ''
            
        try:
            self.client_socket.connect((self.host, self.port))

            if isinstance(message, list):
                for s_message in message:
                    # time.sleep(0.1)
                    self.client_socket.sendall(s_message.encode())
            else:
                self.client_socket.sendall(message.encode())

            self.client_socket.settimeout(5.0)

            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                total_data += data.decode()
                # print(data.decode())
        except KeyboardInterrupt:
            pass
                    # self.client_socket.close()
        finally:
            self.client_socket.close()
            return total_data



if __name__ == "__main__":
    client = Client(HOST, PORT)
    messages = ['3;0;1;28;0;7;5;0;', '10;0;1;26;0;8;3;0;', '18;0;6;28;0;23;5;0;', '7;0;1;28;0;9;3;0;', '22;0;6;28;0;23;3;0;', '7;0;6;28;0;23;5;0;', '2;0;1;26;0;7;5;0;', '10;0;1;26;0;7;4;0;', '7;0;1;26;0;8;3;0;', '13;0;1;28;0;7;4;0;']
    print(client.send_message(messages))
    # client.send_message(messages)
    # "4;0;1;28;0;5;3;0;\x00"

# SSL = True  # The port used by the server


# try:
#     # create socket
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     if SSL:
#         context = ssl.create_default_context()
#         working_dir = os.path.dirname(os.path.abspath(__file__))
#         server_cert = os.path.join(working_dir, 'cert.pem')
#         context.check_hostname = False
#         context.verify_mode = ssl.CERT_NONE
#         client_socket = context.wrap_socket(client_socket, server_hostname=HOST)

#     # connect to the server
#     client_socket.connect((HOST, PORT))
#     print("Connected to the server")
#     # 13;0;23;11;0;16;5;0;
#     # create and send message to the server
#     message= "4;0;1;28;0;5;3;0;\x00"
#     client_socket.send(message.encode())

#     data_x = ''
#     while True:
#     # Receive data from the server (optional)
#         data = client_socket.recv(1024)
#         if len(data) <= 0:
#             break
#         data_x += data.decode()
    
#         print("Received from server:", data_x)
# except socket.error as e:
#     raise e
# except KeyboardInterrupt as e:
#     print("socket closed")
#     client_socket.close()
#     raise e

# finally:
#     client_socket.close()
#     print("Socket Closed")

