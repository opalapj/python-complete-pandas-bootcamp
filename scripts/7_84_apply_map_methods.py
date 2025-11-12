import pandas as pd


sales = pd.read_csv("data/sales.csv", index_col=0)
summer = pd.read_csv("data/summer.csv")

sales.info()
sales.min()
sales.min(axis=1)
pd.set_option("expand_frame_repr", False)


# Apply method - apply function along an axis (here: dataframe's series and series' subscriptable values).
# Dataframe's series.
def diff(series):
    return series.max() - series.min()


sales.apply(diff)
sales.apply(lambda series: series.max() - series.min())
sales.apply(diff, axis=1)
sales.apply(lambda series: series.max() - series.min(), axis=1)
summer.apply(lambda series: series[0])
summer.apply(lambda series: series[0], axis=1)

# Series' subscriptable (e.g. string) and single values (e.g. integer).
summer["Athlete"].apply(lambda value: value[0])  # Legal: 'str' object is subscriptable.
summer["New"] = 9
summer["New"].apply(
    lambda value: value[0]
)  # TypeError: 'int' object is not subscriptable.
summer["New"].apply(lambda value: value / 9 + 1)  # Legal: 'int' object is single value.
summer["New"] = "ABC"
summer["New"].apply(lambda value: value[0])  # Legal: 'str' object is subscriptable.

# Map method - map series' values according to input function.
summer["Athlete"].map(lambda value: value[0])
summer["Athlete"].apply(lambda value: value[0])  # Apply method can do the same.
summer["Athlete"].map(lambda value: "{} was a medalist.".format(value))
summer["Athlete"].apply(
    lambda value: "{} was a medalist.".format(value)
)  # Apply method can do the same.
summer["Athlete"].map("{} was a medalist.".format)
summer["Athlete"].apply("{} was a medalist.".format)  # Apply method can do the same.
summer["Athlete"].map({"HAJOS, Alfred": "index zero", "DRIVAS, Dimitrios": "index two"})
summer["Athlete"].apply(
    {"HAJOS, Alfred": "index zero", "DRIVAS, Dimitrios": "index two"}
)  # Apply method cannot do the same!

# Map method - map series' values from data frame's series to input function.
summer.iloc[:, 1:3].apply(
    lambda series: series[0]
)  # Apply method takes first values from series.
summer.iloc[:, 1:3].map(
    lambda value: value[0]
)  # Applymap methed takes first character from each values from these series.
sales.map(lambda value: 0.4 * value - 5)
