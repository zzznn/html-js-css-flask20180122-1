from pymongo import MongoClient
from datetime import datetime
client = MongoClient('127.0.0.1', 27017)
db_name = 'Mytest'
db = client[db_name]

def add(name ,password ,email , qq="null", tel="null", age="null",address="null"):   #插入新的纪录
    print("add（）函数，用于插入新的纪录")
    result = db.user.insert_one(
        {
            "name": name,
            "password": password,
            "email": email,
            "qq": qq,
            "tel": tel,
            "age": age,
            "address": address
        })

def ensure_index(): # 创建1个唯一索引，用了name，因此注册时用户名不能重复
    a = db.user.ensure_index('name', unique=True)
    print(a)


def Select(name,password):   #查找信息 name（用户名）和 password（密码）
    #print("select（）函数，用于查找信息")
    cursor = db.user.find_one({"name": name, "password": password})
    a = cursor
    print("登陆信息查询结果：")
    print(a)
    if a == None:     #判断是否存在 name/password = 输入，这里如果返回None 则说明没有查询到，这时候函数就返回一个 NO
        #print("NO")
        return "NO"
    else:              #这里如果返回有信息，则说明存在 name/password = 输入，这时候函数就返回一个 OK
        #print("OK")
        return "OK"


def SelectName(name):   #查找信息 name（用户名），这里我们设置了唯一约束name，在注册的时候，先验证是否存在用户了
    #print("select（）函数，用于查找信息")
    a = db.user.find_one({"name": name})
    b = a
    print(b)
    if b == None:   #判断是否存在 name = 输入 ，这里如果返回 None 则说明没有，这时候函数就返回一个 NO
        #print("NO")
        return "NO"
    else:              #这里如果返回有信息，则说明存在 name = 输入，这时候函数就返回一个 OK
        #print("OK")
        return "OK"

def Update():  #更新信息
    print("Update（）函数，用于更新信息")
    result = db.user.update_one(
        {"name": "kevin"},
        {
            "$set":     # $set将在没有该字段的时候新建这个字段 #
                {"age": "18"}
        }
    )


def Replace():  #用于替换,更新操作后，被修改的文档将只剩下修改的项
    print("Replace（）函数，用于替换信息")
    result = db.user.replace_one(
        {"name": "kevin"},
        {
            "name": "tone",
            "age": "2"
            }
    )

def Delete(name,password):    # 将删除所有符合条件的文档 #
    print("Delete（）函数，用于删除信息")
    print("name = ",name)
    result = db.user.delete_many({"name":name,"password":password})


# 测试函数是否可行
#a = "kevin"
#b = add('kevin','123456',"zzznn@163.com")
#print(b)
#c = SelectName('kevin2')
#print(c)
#Update()
#Replace()
#Delete("kevin4","123456")
#CreateIndex()


