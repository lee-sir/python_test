import socket

server =socket.socket()

server.bind(('localhost',6969))#绑定监听对象

server.listen()#监听
print("准备开始接收消息了！！！！")

con,addr=server.accept()#等待消息

print(con,addr)

data=con.recv(1024)

print("接收到的消息是",data)

server.close()
