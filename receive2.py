import time
from connection.multicast_server import multicastServer

def receive_data():
        send_sock = multicastServer.create_server_socket()
        data, addr = multicastServer.receive_from(send_sock)
        return (data, addr)


if __name__ == "__main__":
    while True:
        data, addr = receive_data()
        print(f'Data received:{data} from addr:{addr}')