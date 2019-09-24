import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data=pd.read_csv("风景名胜区.csv",encoding="gbk")
print(data)
#判断是否重复
print(data.duplicated())
#判断是否空值
print(data.isnull().sum())
#用替换法填充空值,用均值填充
area=int(data['总面积(平方公里)'].mean())
print(area)
num=data['游客量(万人次)'].mean()
num=float("{:.1f}".format(num))#保存一位小数
print(num)
dct={"总面积(平方公里)":area,"游客量(万人次)":num}
data.fillna(dct,inplace=True)
print(data)
#提取河北省的数据分组
datagroup=data.groupby(by='省份')
hebei=dict([x for x in datagroup ])['河北']
print(hebei)
#显示中文
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(10,5))
# 画条形图
# labels=hebei['名称'].values
# x=np.arange(len(labels))
# dict1=hebei['总面积(平方公里)'].values
# dict2=hebei['游客量(万人次)'].values
# plt.bar(x,dict1,width=0.3,label='总面积')
# x=[x+0.3 for x in x]
# plt.bar(x,dict2,width=0.3,label='游客量')
# plt.xticks(np.arange(10),labels=labels)
# plt.ylabel('单位：平方千米/万人次')
# plt.title('河北景点面积及旅客数量')
# plt.legend(loc="upper right")
# plt.show()
#print(labels)
#画饼图
plt.figure(figsize=(12,6))
num=hebei['游客量(万人次)'].values
all_num=hebei['游客量(万人次)'].sun()
percent=(num/all_num)*100
labels=hebei['名称'].values
plt.pie(x=percent,labels=labels,autopct="%3.2f%%",shadow=True,startangle=90)
plt.legend(labels=labels,loc="upper left")
plt.show()
