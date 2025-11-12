import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

titanic["age"].fillna(titanic["age"].mean(), inplace=True)
titanic["sibsp"] + titanic["parch"]
titanic["sibsp"].add(titanic["parch"])
titanic["no_relat"] = titanic["sibsp"].add(titanic["parch"])
1912 - titanic["age"]
titanic["YoB"] = titanic["age"].sub(1912, fill_value=None).mul(-1)

sales = pd.read_csv("data/sales.csv", index_col=0)

sales["Mon"] + sales["Thu"]
sales["Mon"].add(sales["Thu"], fill_value=0)
sales["perc_Bonus"] = [0.12, 0.15, 0.10, 0.20]
sales["Thu"] * sales["perc_Bonus"]
sales["Thu"].mul(sales["perc_Bonus"], fill_value=0)
sales.iloc[:, :-1].sum(axis=1)
sales.iloc[:, :-1].sum(axis=1).mul(sales["perc_Bonus"])
sales["Bonus"] = sales.iloc[:, :-1].sum(axis=1).mul(sales["perc_Bonus"])
