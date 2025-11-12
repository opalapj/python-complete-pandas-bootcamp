import numpy as np
import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

titanic["no_relat"] = titanic["sibsp"].add(titanic["parch"])
titanic["no_relat"] == 0
np.where(titanic["no_relat"] == 0, "Yes", "No")
pd.Series(np.where(titanic["no_relat"] == 0, "Yes", "No"))
# titanic['no_relat'].map(lambda x: 'No' if x else 'Yes')
titanic["alone"] = pd.Series(np.where(titanic["no_relat"] == 0, "Yes", "No"))
titanic["child"] = pd.Series(np.where(titanic["age"] < 18, "Yes", "No"))
