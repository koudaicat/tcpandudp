import socket

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.sendto(b"hahahaa",("127.0.0.1",7788))
    udp_socket.close()






if __name__ == '__main__':
    main()

