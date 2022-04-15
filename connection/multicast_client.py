import socket
import struct



'''
The first step to establishing a multicast receiver is to create the UDP socket.
After the regular socket is created and bound to a port, it can be added to the multicast group
'''

class multicastClient():

    def create_client_socket():
        try:
            # Create the datagram socket
            client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            # Set a timeout so the socket does not block indefinitely when trying
            # to receive data.
            client_sock.settimeout(0.2)
            # Set the time-to-live for messages to 1 so they do not go past the
            # local network segment.
            ttl = struct.pack('b', 2)
            client_sock   .setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
            return client_sock
        except Exception as e:
            print(e)
            return None

    def receive_from(sock, bufsize=1024):
        try:
            # Receive data from client
            data, address = sock.recvfrom(bufsize)
            return (data, address)
        except Exception as e:
            print(e)

    def send_to(sock, message, multicastGroup):
        try:
            # Send data to client
            sock.sendto(message.encode('utf-8'), multicastGroup)
        except Exception as e:
            print(e)
