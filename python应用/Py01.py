import pandas as pd


df=pd.read_csv("data/stock.csv")
print(df)
"""
#获取第二列数据类型
print(df['date'].dtype)
#转换数据类型
df['date']=df.to_datetime(df['date'])      # 有错
print(df['date'].dtype)
#得到datafrom对象所有列的数据类型
print(df.info())
#提取时间的年月日 构建datatimeindex
dtindex=pd.DatetimeIndex(df['date'])
print(dtindex)
print(dtindex.year)  #提取年
print(dtindex.month) #提取月
"""
#第二种方法
df.set_index('date',inplace=True)
print(df.index)
print(df)

#第三种方法
year=[i.year for i in df['data']]
print(year)




