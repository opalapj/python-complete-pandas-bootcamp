# https://pandas.pydata.org/docs/user_guide/advanced.html

import pandas as pd


list_1 = [1, 2, 3]
pd.Index(list_1)
list_2 = ["m", "t", "w"]
pd.Index(list_2)
pd.Index(range(1, 4))
index_1 = pd.Index(range(1, 4))
index_2 = pd.Index(list_2, name="days")
pd.Series([34, 32, 21], list_1)
pd.Series([34, 32, 21], list_2)
pd.Series([34, 32, 21, 19], list_2)  # Length of values does not match length of index.
pd.Series([34, 32], list_2)  # Length of values does not match length of index.
