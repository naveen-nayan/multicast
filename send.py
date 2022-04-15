import time
from connection.multicast_client import multicastClient

def send_data(message):
        send_sock = multicastClient.create_client_socket()
        group = ('224.0.0.0', 10000)
        multicastClient.send_to(send_sock, message, group)


if __name__ == "__main__":
    while True:
        data = "Hello"
        print(f'sending data:{data}')
        send_data(data)
        time.sleep(1)