import socket
import struct



'''
The first step to establishing a multicast receiver is to create the UDP socket.
After the regular socket is created and bound to a port, it can be added to the multicast group
'''

class multicastServer():

    def create_server_socket(Address='224.0.0.0', Port=10000):
        try:
            # Create the socket
            server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            # reused address immediately instead of it being stuck in the TIME_WAIT state
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # Bind to the server address
            server_sock.bind(('', Port))
            group = socket.inet_aton(Address)
            mreq = struct.pack('4sL', group, socket.INADDR_ANY)
            # Add membership
            server_sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
            return server_sock
        except Exception as e:
            print(e)
            return None    

    def receive_from(sock, bufsize=1024):
        try:
            # Receive data from client
            data, address = sock.recvfrom(bufsize)
            return (data.decode('utf-8'), address)
        except Exception as e:
            print(e)

    def send_to(sock, address, message='ack'):
        try:
            # Send data to client
            sock.sendto(message.encode('utf-8'), address)
        except Exception as e:
            print(e)
