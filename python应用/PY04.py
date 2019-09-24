import pandas as pd

from python应用.Py03 import data_group

df=pd.DataFrame({'key1':['A','A','B','B','B'],
                 'key2':['one','two','one','two','one'],
                 'data1':['2','3','4','6','8'],
                 'data2':['3','5','6','3','7']})
se=pd.Series(['a','b','c','a','b'])
group_obj=df.groupby(by=se)
for i in group_obj:
    print(i)

data1=dict([x for x in data_group])['A']
print(data1)
data2=dict([x for x in data_group])['B']
print(data2)
