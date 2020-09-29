import socket# 生成链接对象
client = socket.socket()#生成socket链接对象
client.connent(("ip地址"，端口号))#和目标主机建立连接
client,send("hello world".emcode())#向对方发送数据
client.close()