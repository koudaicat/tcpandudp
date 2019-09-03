import socket
def main():
    #创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #链接服务器
    server_ip = input("请输入要链接的服务器ip")
    server_port = int(input("请输入要链接服务器的port："))
    server_addr = (server_ip,server_port)
    tcp_socket.connect(server_addr)
    #发送数据/接收数据
    send_data = input("请输入要发送的数据：")
    tcp_socket.send(send_data.encode("utf-8"))

if __name__ == '__main__':
    main()

'''tcp客户端是需要被服务的一方'''
