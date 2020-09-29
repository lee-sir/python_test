class Card(object):
	"""docstring for Card"""
	def __init__(self, num,pwd,ban):
		self.num=num #卡号
		self.pwd=pwd #密码
		self.__ban=ban #余额 双下划线，私有属性（且只能在类的内部被访问）
	def cun(self):
		print("存款")
	def getban(self,numm,pwdd):
		if numm==self.num and pwdd==self.pwd:
			return self.__ban
		else:
			return "you are error!"
card=Card("123131","1231",12345) #开卡
print(card.getban("123131","1231"))

#多态，		
	