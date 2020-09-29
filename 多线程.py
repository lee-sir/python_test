import threading
import time


def run(name):

 	print(name,"线程执行")
 	time.sleep(10)

#程序执行时，程序本身就是一个线程，叫主线程
#手动创建的线程叫子线程
#主线程执行的时候，并不会等待子线程执行完毕，就会直接执行后面的代码
#创建线程
t1=threading.Thread(target=run,args=("t1",))
t2=threading.Thread(target=run,args=("t2",))

t1.start()#启动进程
t2.start()

t1.join()#设置子线程执行完毕后再执行主线程
#t2.join()

print("执行完毕")