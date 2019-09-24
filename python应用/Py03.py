import pandas as pd
df1=pd.read_csv("data/mytest.csv")
print(df1)
#按照
data_group=df1.groupby(by='name')
print(data_group)
#使用for循环遍历取得组内元素
for i in data_group:
    print(i)