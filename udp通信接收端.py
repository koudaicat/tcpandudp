import socket

def main():
    #创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定本地信息
    localaddr = ("" ,7788)
    udp_socket.bind(localaddr)
    #等待接收对方数据
    recv_data = udp_socket.recvfrom(1024)
    #打印数据
    recv_msg = recv_data[0]
    send_addr = recv_data[1]
    print('%s:%s' %(str(send_addr),recv_msg.decode("gbk")))
   #关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()

