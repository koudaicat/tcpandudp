import socket
def send_file_2_client(new_client_socket,client_addr):
    #接收客户端发送过来的，要下载的文件名
    file_name = new_client_socket.recv(2024).decode('utf-8')
    print("%s"%(str(client_addr),file_name))
    file_content = None
    #2、打开这个文件，读取数据
    try:
        f = open(file_name,'rb')
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件%s" % file_name)
    #发送文件的数据给客户端
    if file_content:
        new_client_socket.send(file_content)

def main():
    # 创建套接字（相当于买个手机）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定本地信息（即插入手机卡）
    tcp_server_socket.bind('', 7890)
    # 让套接字由主动变为被动 listen(即手机设置响铃)
    tcp_server_socket.listen(128)
    #等待别人电话过来（等待客户端的链接 accept）
    while True:
        new_client_socket, client_addr = tcp_server_socket.accept()
        #调用发送文件函数，完成客户端服务
        send_file_2_client(new_client_socket，client_addr)
        #关闭套接字
        new_client_socket.close()
    tcp_server_socket.close()

