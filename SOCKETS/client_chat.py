import socket
import threading
from netProtocol import create_msg_with_header, recieve_msg

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 12345
STOP_FLAG = False

def do_authenticate(client_socket):
    res = False
    while not res:
        auth_kind_and_params = input('Loging (2 params: username, password) or Signup (3 params: username, password, email)')
        client_socket.send(bytes(create_msg_with_header(auth_kind_and_params), "utf-8"))
        res = bool(recieve_msg(client_socket))
        if not res:
            print('error!!. please try again!!')

# TODO - complete the server size authentication


def send_to_server_thread(client_socket):
    global STOP_FLAG
    do_authenticate(client_socket)
    while True:
        cmd = input('send a msg:')
        client_socket.send(bytes(create_msg_with_header(cmd), "utf-8"))
        if cmd == 'EXIT':
            STOP_FLAG = True
            break


def receive_from_server_thread(client_socket):
    global STOP_FLAG
    while True:
        msg_from_server = recieve_msg(client_socket)
        print(msg_from_server)
        if STOP_FLAG:
            break


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

recieve_thread = threading.Thread(target=receive_from_server_thread, args=(client_socket,))
sending_thread = threading.Thread(target=send_to_server_thread, args=(client_socket,))

recieve_thread.start()
sending_thread.start()
