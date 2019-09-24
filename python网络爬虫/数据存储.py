from pymongo import *
#建立和MongoDB服务器连接
client=MongoClient('127.0.0.1',27017)
#第二种
#client=MongoClient()
print(client)from pymongo import *
#建立和MongoDB服务器连接
client=MongoClient('127.0.0.1',27017)
#第二种
#client=MongoClient()
print(client)

#获取数据库
db=client.itcast
print(db)
print(type(db))
#方法二
#db1=client['itcast']

#获取集合
col=db.stu
print(col)

#添加数据
col.insert({"name":"itcast","age":15})
#添加多条数据

#更新数据
col.update_one({"age":15},{"$set":{"age":100}})