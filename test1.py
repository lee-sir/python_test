#fh1=open(r"D:\Worker Space\Python_test\001.txt","r",encoding='UTF-8')#r第一个是转义的意思，
#第二个是read，fh1表示是文件的句柄
#rb 的意思是读取二进制文件，wb是写入二进制

#data=fh1.read()
#data1=fh1.readline()#按行读取
#data2=fh1.readline()
#data1=fh1.readlines()#按行读取所有
#print(data1)

#fh1.close()#文件操作完毕后关闭资源
#for i in fh1:读取大文件的方法
#   print(i)
#fh1.close()
#====================================================
fh=open(r"D:\Worker Space\Python_test\002.txt",'a',encoding='UTF-8')
#w-writte如果文件存在，就重新写入，如果文件不存在，就创建一个新的文件
#a-appent 文件追加写入
data=" 文本测试----亲爱的小鱼,wohenxihaun"+'\n'+"这是一个下雨天"+'\n'
fh.write(data)#括号内可以加变量，可以直接是文本
fh.close()