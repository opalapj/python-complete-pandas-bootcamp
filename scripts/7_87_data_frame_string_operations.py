import pandas as pd


summer = pd.read_csv("data/summer.csv")

type("Hello World")
hello = "Hello World"
len(hello)
hello.lower()
hello.upper()
hello.split(" ")
hello.replace("Hello", "Hi")

names = summer.loc[:9, "Athlete"].copy()
type(names)
names.dtypes
type(names[0])

names.lower()  # Illegal
names.apply(lambda value: value.lower())  # It can be done this way.
names.str.lower()  # But this way is more effective.
names.str.title()

summer["Event"].str.split()
summer["Event"].str.contains("100M")
summer.loc[summer["Event"].str.contains("100M")]
