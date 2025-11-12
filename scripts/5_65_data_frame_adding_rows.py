# https://pandas.pydata.org/docs/user_guide/merging.html#appending-rows-to-a-dataframe

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

dic = {
    "Player": player,
    "Nationality": nationality,
    "Club": club,
    "World_Champion": world_champion,
    "Height": height,
    "Goals_2018": goals,
}
players = pd.DataFrame(data=dic)

new_player1 = ["Sergio Ramos", "Spain", "Real Madrid", True, 1.84, 5]
new_player2 = ["Mohamed Salah", "Egypt", "FC Liverpool", False, 1.75, 44]
new_player3 = ["Luis Suarez", "Uruguay", "FC Barcelona", False, 1.82, 31]

# 1st way - single row adding.
new_team_1 = players.copy()
new_team_1.loc[len(new_team_1)] = new_player1
new_team_1.loc["new_player"] = (
    new_player1  # It is possible to add new row with dedicated index labeb.
)

# 2nd way - single & multiple rows adding.
# Create new df with single player.
new_players = pd.DataFrame(data=[new_player1], columns=players.columns)

new_team_2 = players.append(new_players, ignore_index=True)  # Old method.
new_team_3 = pd.concat([players, new_players], ignore_index=True)  # New method.
new_team_3.equals(new_team_2)

# Create new df with multiple players.
new_players = pd.DataFrame(data=[new_player2, new_player3], columns=players.columns)

new_team_4 = pd.concat([players, new_players], ignore_index=True)

# Adding single empty row.
pd.concat([players, pd.Series().to_frame().T], ignore_index=True)
pd.concat([players, pd.DataFrame(index=[0])], ignore_index=True)
pd.concat([players, pd.Series(name="NameOfNewRow").to_frame().T])
pd.concat([players, pd.DataFrame(index=["NameOfNewRow"])])

# Adding multiple empty rows.
pd.concat([players, pd.DataFrame(index=range(0, 3))], ignore_index=True)
