import pandas as pd


table1 = pd.read_csv("data/table1.csv")

table1.describe(include="object")
table1.pivot(index="Country", columns="Medal", values="Count").fillna(0)

table2 = pd.read_csv("data/table2.csv")


# Index contains duplicate entries, cannot reshape.
table2.pivot(index="Country", columns="Medal", values="Count").fillna(0)


table2.pivot_table(
    index="Country", columns="Medal", values="Count", aggfunc="sum", fill_value=0
)
table2.groupby(["Country", "Medal"]).Count.sum().unstack(-1, fill_value=0)


table2.pivot_table(
    index="Country", columns="Medal", values="Count", aggfunc="sum", fill_value=0
)[["Gold", "Silver", "Bronze"]].sort_values(
    ["Gold", "Silver", "Bronze"], ascending=False
)
table2.groupby(["Country", "Medal"]).Count.sum().unstack(-1, fill_value=0)[
    ["Gold", "Silver", "Bronze"]
].sort_values(["Gold", "Silver", "Bronze"], ascending=False)
