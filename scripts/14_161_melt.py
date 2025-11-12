import pandas as pd


table_2012 = pd.read_csv("data/table_2012.csv")

pd.melt(table_2012, "Country")

pd.melt(
    frame=table_2012,
    id_vars="Country",
    value_vars=None,
    var_name="Medal",
    value_name="Count",
)

table_2012.set_index("Country").stack().reset_index()
