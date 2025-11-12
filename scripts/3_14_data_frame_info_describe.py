# https://pandas.pydata.org/docs/user_guide/dsintro.html#console-display
# https://pandas.pydata.org/docs/user_guide/basics.html#summarizing-data-describe

import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

titanic.info()

titanic.describe()
titanic.describe(percentiles=[0.1, 0.2, 0.3])
titanic.describe(include="all")
titanic.describe(include="number")  # For float & int together.
titanic.describe(include="float")
titanic.describe(include="int")
titanic.describe(include="object")
