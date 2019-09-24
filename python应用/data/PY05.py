import pandas as pd

import numpy as np

ser_obj=pd.Series(np.range(1,6),index=[5,3,0,4,2])

ser_obj.sort_index()