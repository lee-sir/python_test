import pymysql

#链接数据库  主机地址 端口号3306 用户名 密码 数据库名

db=pymysql.Connect(host="localhost",port=3306,user="test",passwd="123321",db="stu",charset="utf8")

#创建一个游标对象cursor()
cursor=db.cursor()

#1定义sql语句 创建表
sql="""create table student(
id int not null,
name varchar(20),
age int
)"""

#2向表格添加数据
sql='''insert into student(id,name,age)
values(1,"zhangsan",12)

'''

#3查询数据
sql='''select * from student

'''
#4更新操作
sql='''update student set age=age+1

'''

#5删除操作
sql='''delete from student where name="lisi"

'''

#data=cursor.fetchone()单个对象/fetchall()多个对象  print(data)/print(data[1])获取一行数据

cursor.execute(sql)#执行sql语句
db.commit()
db.close()




