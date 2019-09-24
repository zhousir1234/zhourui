import pandas as pd
import numpy as pd
df_obj=pd.DataFrame({"类别":['小说','散文随笔','青春文学','传记'],
                     "书名":[np.NAN,'《皮囊》','《旅程结束时》','《老舍自传》'],
                     "作者":['老舍',None,'张其鑫','老舍']})
df_obj=pd.DataFrame({'A':[1,2,3,np.NAN],
                     'B':[np.NAN,4,np.NAN,6],
                     'C':['a',7,8,9],
                     'D':[np.NAN,2,3,np.NAN]})
print(df_obj)
print(df_obj.fillna('66.0'))
dict={'A':50.0,'B':60.0,'C':66.0}
print(df_obj.fillna(dict))
