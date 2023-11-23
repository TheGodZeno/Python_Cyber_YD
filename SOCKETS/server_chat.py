import socket
import threading
from netProtocol import create_msg_with_header, recieve_msg

CLIENT_COUNTER = 1
CLIENTS = {}

def session_with_client(client_socket, client_name):
    while True:
        client_msg = recieve_msg(client_socket)
        print(client_msg)
        if client_msg == 'EXIT':
            CLIENTS.pop(client_name)
            client_socket.close()
            for s in CLIENTS.values():
                s.send(bytes(create_msg_with_header(f'client num.{client_name} has left the building!!'), "utf-8"))

        else:
            for s in CLIENTS.values():
                s.send(bytes(create_msg_with_header(f'client num.{client_name} say: {client_msg}'), "utf-8"))




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 12345))
s.listen(4)

while True:
    print('server is listening...')
    client_socket, address = s.accept()
    print(f'connection {address} has been established')
    client_name = f'client {CLIENT_COUNTER}'
    CLIENTS[client_name] = client_socket
    CLIENT_COUNTER+=1
    client_thread = threading.Thread(target=session_with_client, args=(client_socket, client_name))
    client_thread.start()


s.close()