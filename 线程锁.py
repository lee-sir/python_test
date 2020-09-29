import threading

lock=threading.Lock()#创建一个线程锁

num=100

def run(name):
	lock.acquire()# 设置锁
	global num#设置num为全局变量
	num=num-1
	print("线程",num,"走了一下，目前为：",num)
	lock.release()#释放锁

#创建100个线程
for i in range(100):
	t=threading.Thread(target=run,args=(i+1,))
	t.start()

#全局解释器锁
"""不管系统中cpu核心数量是多少，都保证Python程序中同一时间点只能执行一个线程"""
#使用多进程解决GIL的问题