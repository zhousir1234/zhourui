import pandas as pd
df1=pd.DataFrame({'A':['A1','A2','A3','A4'],
                  'B':['B1','B2','B3','B4'],
                  'C': ['C1', 'C2', 'C3', 'C4'],
                  'D': ['D1', 'D2', 'D3', 'D4']},index=[1,2,3,4])
print(df1)
df2=pd.DataFrame({'B':['B2','B4','B6','B8'],
                  'D': ['D2', 'D4', 'D6', 'D8'],
                  'F': ['F2', 'F4', 'F6', 'F8']},index=[2,4,6,8])
print(df2)
print(pd.concat([df1,df2],axis=1,join='inner'))
print(pd.concat([df1,df2],axis=1,join='outer'))
print(pd.concat([df1,df2],axis=0,join='inner'))
