import pandas as pd

from sqlalchemy import create_engine
df=pd.read_csv('D:\\PYTHON\\python\\data.csv')
df.drop(columns='Unnamed: 0',axis=1,inplace=True)
print(df)
engine = create_engine('mysql+pymsql://root:123456@127.0.0.1:3306/douban?charset=utf8')
print(engine)
# con.execute("use mysql")  # 使用数据库
# con.execute("drop table if exists t_doubantop")
# 创建一个表 对应的信息有rank name date country type charactor remark score count
# sql = '''create table t_doubantop(rank_list VARCHAR(10),name VARCHAR(40) NOT NULL,date VARCHAR(20),country VARCHAR(20),
# type VARCHAR(20),charactor VARCHAR(100),remark VARCHAR(100),score VARCHAR(40),count VARCHAR(40))'''
# con.execute(sql)
#     # 导入数据库

