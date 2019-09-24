import pandas as pd


df=pd.read_csv("data/shu.csv",encoding='gbk')
#print(df)
#删除最后一行

df.drop(labels=70679,axis=0,inplace=True)
#print(df)
#将支付时间这列格式转换为时间格式 to datatime

df['支付时间']=pd.to_datetime(df['支付时间'])
print(df['支付时间'].dtype)#对象打点
#提取2017年4月份的销售总额 （4月份应付总额的和）
#提示：将支付时间这列设为dfl的索引（时间戳索引）

df.set_index('支付时间',inplace=True)
print(df)
#获取2017年4月份的数据   不要sum的括号的时候显示  应付金额的值
print(df['2017-04']['应付金额'].sum())




