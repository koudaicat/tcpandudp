import socket
def main():
    #创建套接字（相当于买个手机）
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定本地信息（即插入手机卡）
    tcp_server_socket.bind('',7890)
    #让套接字由主动变为被动 listen(即手机设置响铃)
    tcp_server_socket.listen(128)
    #循环目的，调用多次accept，从而为多个客户端服务
    while True:
        print("等待一个新客户端到来")
        #等待客户端的链接 别人打电话
        new_client_socket,client_addr = tcp_server_socket.accept()
        print("一个新客户端一已经到来%s" %str(client_addr))
        #循环目的，为同一个客户端服务多次
        while True:
            #接收客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)
            print("客户端送过来的请求是：%s" %recv_data.decode("utf-8"))
            #如果客户端解堵塞，那么有2种方式：
            #1、客户端发送过来数据
            #2、客户端调用close导致 这里recv解毒舌
            if recv_data:
                #回送一部分数据给客户端
                new_client_socket.send("hahahah".encode("utf-8"))
            else:
                break
        #关闭套接字
        new_client_socket.close()

        if __name__ == '__main__':
            main()

