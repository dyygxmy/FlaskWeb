# 对象关系映射(ORM)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@localhost/test"
# 添加配置
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db=SQLAlchemy(app)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"



class User(db.Model):
    '''
        primary_key	如果设为 True,这列就是表的主键
        unique	    如果设为 True,这列不允许出现重复的值
        index	    如果设为 True,为这列创建索引,提升查询效率
        nullable	如果设为 True,这列允许使用空值;如果设为 False,这列不允许使用空值
        default	    为这列定义默认值
    '''
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(45),unique=True)
    password = db.Column(db.String(45))
    def __int__(self,username,password):
        self.username = username
        self.password = password

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 0

    def isExisted(self):
        temUser = User.query.filter_by(username=self.username,password=self.password).first()
        if temUser is None:
            return 0
        else:
            return 1


class Entry(db.Model):
    '''
        primary_key	如果设为 True,这列就是表的主键
        unique	    如果设为 True,这列不允许出现重复的值
        index	    如果设为 True,为这列创建索引,提升查询效率
        nullable	如果设为 True,这列允许使用空值;如果设为 False,这列不允许使用空值
        default	    为这列定义默认值
    '''
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text) # Text类型不能定义unique
    sender = db.Column(db.String(45))
    status = db.Column(db.INT)
    def __int__(self,content,sender):
        self.content = content
        self.sender = sender

    def add(self):
        try: # 错误处理没啥用 数据类型不对会自动转换，转换不了的就不存储，sender有重复也不存储，但这些都不会抛出异常
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 222

    def create(self):
        try: # 表格存在也不会抛出异常
            db.create_all() # 创建对象，用在这里是创建表，表名默认是类名
        except Exception as e:
            return e
        return 222

    def drop(self):
        db.drop_all()


def getAllEntry():
    Enlist = []
    Enlist = Entry.query.filter_by().all()
    return Enlist


class Item(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    context=db.Column(db.String(128))
    sender_id=db.Column(db.Integer)
    def __int__(self,context,sender_id):
        self.context=context
        self.sender_id=sender_id

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 0


class UIRelation(db.Model): # 新建一个表来过渡多对多关系
    id=db.Column(db.Integer,primary_key=True)
    uid=db.Column(db.Integer)
    iid=db.Column(db.Integer)

# db.create_all() # 创建所有表，这里有user,entry,item

# u = User(username="jikexueyuan",password="123456")
# print(u.isExisted())
# u.username="zhangsan"
# u.password="642534"
# print("add:",u.add())

# en = Entry()
# print("create",en.create())
# en.content=123456
# en.sender=43547575648
# en.status=555
# print("add:",en.add())
# enList=getAllEntry()
# for item in enList:
#     print(item.content,item.sender,item.status)

# i = Item(context="我今天学习python课",sender_id=1)
# i = Item(context="休息一天",sender_id=1)
# print(i.add())

# a = User.query.filter_by(username="jikexueyuan").first()
# print(a.id)
# list = Item.query.filter_by(sender_id=a.id).all()
# for each in list:
#     print(each.context)