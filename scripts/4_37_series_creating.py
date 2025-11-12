# https://pandas.pydata.org/docs/user_guide/dsintro.html#series

import numpy as np
import pandas as pd


# By read_csv method.
path = "data/summer.csv"
s = pd.read_csv(path, usecols=["Athlete"])  # Read one column but still as a data frame.
s = pd.read_csv(
    path, usecols=["Athlete"], squeeze=True
)  # That's it, but in old version.
s = pd.read_csv(path, usecols=["Athlete"]).squeeze("columns")  # Uff, that's it.
s = pd.read_csv(path, usecols=["Athlete", "Country"])  # Read selected columns, 1st way.
s = pd.read_csv(
    path, usecols=lambda x: x.upper() in ["ATHLETE", "COUNTRY"]
)  # Read selected columns, 2nd way.
s = pd.read_csv(
    path, usecols=["Country", "Athlete"]
)  # Sequencing in this way does not work.
s = pd.read_csv(path, usecols=["Athlete", "Country"])[
    ["Country", "Athlete"]
]  # But in this way does.

# By Series class instantiating.
s1 = pd.Series([10, 25, 6, 36, 2])
s2 = pd.Series([10, 25, 6, 36, 2], index=["Mon", "Tue", "Wed", "Thu", "Fri"])
s3 = pd.Series(
    [10, 25, 6, 36, 2], index=["Mon", "Tue", "Wed", "Thu", "Fri"], name="Sales"
)

# From Numpy Array.
s4 = np.array([10, 25, 6, 36, 2])
s4 = pd.Series(s4)

# From list.
s5 = [10, 25, 6, 36, 2]
s5 = pd.Series(s5)

# From dictionary.
dic = {"Mon": 10, "Tue": 25, "Wed": 6, "Thu": 36, "Fri": 2}
s6 = pd.Series(dic)
s6 = pd.Series(dic, index=["Mon", "Tue", "Wed", "Fri", "Sat", "Sun"])
s6 = pd.Series(dic, index=[1, 2, 3, 4, 5])

s7 = pd.Series(data=["Madrit", "Paris"], index=["Spain", "France"])
