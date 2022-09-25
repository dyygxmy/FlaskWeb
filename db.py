# 管理与mysql数据库的交互

import pymysql

# 连接数据库
conn = pymysql.connect(host="localhost",user="root",password="123456",database="test")

# 建立游标
cur = conn.cursor()

def addUser(username,password):
    sql = "insert into user(username,userpassword) values(\"%s\",\"%s\")"%(username,password)
    cur.execute(sql)
    conn.commit()
    conn.close()

def isExisted(username,password):
    sql = "select * from user where username = \"%s\" and userpassword = \"%s\" "%(username,password)
    cur.execute(sql)
    result = cur.fetchall()
    if len(result) == 0:
        return False
    else:
        return True





# name = input("请输入插入的学生名: ")
# # sql语句
# sql = "select * from student"
# insert_sql = "insert into test.student(name) values(\"%s\");"%(name)
#
# # 执行语句
# cur.execute(insert_sql)
# conn.commit() # pymysql里是通过连接提交的，有的是通过游标提交的
#
# cur.execute(sql)
#
# # 获取结果
# result = cur.fetchall()
#
# cur.close()
#
# for row in result:
#     print(row[0],row[1])
