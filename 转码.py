#python中的字符串的两种类型：bytes,str,str存储Unicode类型，bytes存储byte类型

#字符串转byte----编码
a="我爱北京天安门"
b=a.encode("utf-8")#转成字节码

print(b)

#byte转字符串---解码
c=b.decode("utf-8")
print(c)

#编码方式和解码方式要一致
"""
数据挖掘-爬虫（爬虫，爬虫框架，数据清洗，数据库）
web编程-做网站（前端，web框架，数据库）
数据分析（数学，统计学，行业知识，数据挖掘）
ALTER USER 'test'@'localhost' IDENTIFIED WITH mysql_native_password BY '123321';

"""