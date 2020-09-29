class Dog(object):
	typee="宠物"#类变量
	
	def __init__(self,name,age,color):#初始化方法
		self.name=name#实例变量（属性）
		self.age = age
		self.color=color
	def eat(self):
		print(self.name,'在啃骨头')

	def run(self,speed):
		print(self.name,"在跑，速度：",speed)
#实例化对象
dog=Dog("小黑",3,"紫色")
print(dog.name)
dog.eat()
dog.run("100m/s")