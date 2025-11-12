import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


pd.options.display.width = None

summer = pd.read_csv("data/summer.csv")
winter = pd.read_csv("data/winter.csv")
dic = pd.read_csv("data/dictionary.csv")

# codes = pd.read_html('https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes')
# codes = codes[0].iloc[:, [0, 4]].copy()
# codes = codes.droplevel(-1, axis=1)
# codes.columns = ['Country', 'Code']
# codes = codes.loc[codes['Code'].map(lambda x: len(x)) <= 3].set_index('Code').sort_index()

codes_dict = {
    "URS": "Soviet Union",
    "GDR": "East Germany",
    "ROU": "Romania",
    "FRG": "West Germany",
    "TCH": "Czechoslovakia",
    "YUG": "Yugoslavia",
    "EUN": "Unified Team",
    "EUA": "Unified Team of Germany",
    "ZZX": "Mixed teams",
    "SRB": "Serbia",
    "ANZ": "Australasia",
    "RU1": "Russian Empire",
    "MNE": "Montenegro",
    "TTO": "Trinidad and Tobago",
    "BOH": "Bohemia",
    "BWI": "West Indies Federation",
    "SGP": "Singapore",
    "IOP": "Independent Olympic Participants",
}
codes = pd.DataFrame(
    index=codes_dict.keys(), data=codes_dict.values(), columns=["Country"]
)


# TODO (1) Merging and concatenating.
olympics = (
    pd.concat([summer, winter], keys=["Summer", "Winter"], names=["Edition"])
    .droplevel(-1)
    .reset_index()
)
olympics = pd.merge(
    olympics, dic.iloc[:, :2], left_on="Country", right_on="Code", how="left"
).drop(columns="Code")

# TODO (2) Rename columns, replace spaces and fill missing country names.

olympics.rename(columns={"Country_x": "Code", "Country_y": "Country"}, inplace=True)
list(filter(lambda x: " " in x, olympics.columns))
list(filter(lambda x: " " in x, dic.columns))
dic.columns = dic.columns.map(lambda x: x.replace(" ", "_"))
missed = (
    olympics[["Code"]]
    .loc[olympics["Country"].isna()]
    .merge(codes, how="left", left_on="Code", right_index=True)
)
olympics["Country"].fillna(missed["Country"], inplace=True)

# TODO (3) Remove rows from olympics where the Country code is unknown.

olympics = olympics.loc[~(olympics.isna().any(axis=1))].reset_index(drop=True)

# TODO (4) Convert the column Medal into an ordered Categorical column ("Bronze" < "Silver" < "Gold").

olympics["Medal"].sort_values(ascending=False)
olympics["Medal"] = pd.Categorical(
    olympics["Medal"], ["Bronze", "Silver", "Gold"], True
)

# TODO (5) What are the Top 10 Countries by total medals?

olympics_top_10 = olympics.loc[
    olympics["Country"].isin(olympics["Country"].value_counts().index[:10])
]
sns.countplot(olympics_top_10, x="Country")
sns.countplot(
    olympics_top_10,
    x="Country",
    hue="Edition",
    order=olympics["Country"].value_counts().index[:10],
    hue_order=["Winter", "Summer"],
)
sns.countplot(
    olympics_top_10,
    x="Country",
    hue="Medal",
    order=olympics["Country"].value_counts().index[:10],
    hue_order=["Gold", "Silver", "Bronze"],
    palette=["gold", "silver", "brown"],
)

# TODO (6) Top 50 Countries and correlations.

olympics["Games"] = olympics["Year"].astype(str) + " " + olympics["City"]
medals_per_country = (
    olympics.groupby("Country")
    .agg(
        Total=("Medal", "count"),
        Gold=("Medal", lambda x: (x == "Gold").sum()),
        Silver=("Medal", lambda x: (x == "Silver").sum()),
        Bronze=("Medal", lambda x: (x == "Bronze").sum()),
        Total_Games=("Games", "nunique"),
    )
    .sort_values("Total", ascending=False)
    .head(50)
)
medals_per_country = (
    medals_per_country.merge(dic, how="left", on="Country")
    .drop(columns="Code")
    .set_index("Country")
)
medals_per_country.rank(ascending=False)

t1 = olympics["Country"].value_counts().rename("Total").to_frame()
t2 = pd.crosstab(index=olympics["Country"], columns=olympics["Gender"])
t3 = pd.crosstab(index=olympics["Country"], columns=olympics["Edition"])
t = t1.merge(t2, on="Country").merge(t3, on="Country")
plt.figure(figsize=(10, 10))
sns.heatmap(t.head(50).rank(ascending=False), annot=True, cmap="RdYlGn_r")

olympics["Sport"].value_counts()
pd.crosstab(olympics["Sport"], olympics["Country"])
