# https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe

import pandas as pd


player = [
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Neymar Junior",
    "Kylian Mbappe",
    "Manuel Neuer",
]
nationality = ["Argentina", "Portugal", "Brasil", "France", "Germany"]
club = ["FC Barcelona", "Juventus FC", "Paris SG", "Paris SG", "FC Bayern"]
world_champion = [False, False, False, True, True]
height = [1.70, 1.87, 1.75, 1.78, 1.93]
goals = [45, 44, 28, 21, 0]

# 1st way - dict of lists.
dic = {
    "Nationality": nationality,
    "Club": club,
    "World_Champion": world_champion,
    "Height": height,
    "Goals_2018": goals,
}
players1 = pd.DataFrame(data=dic, index=player)
players1 = pd.DataFrame(
    data=dic, index=pd.Index(data=player, name="Player")
)  # Index extended by name.

# 2nd way - list of tuples.
z = zip(nationality, club, world_champion, height, goals)
players2 = pd.DataFrame(
    data=list(z),
    index=player,
    columns=["Nationality", "Club", "World_Champion", "Height", "Goals_2018"],
)
players2.equals(players1)

# 3rd way - column by column.
players3 = pd.Series(index=player, data=nationality, name="Nationality").to_frame()
players3["Club"] = club
# ...
