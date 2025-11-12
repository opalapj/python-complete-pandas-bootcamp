import pandas as pd


alphabet = pd.DataFrame(
    {
        "Alphabet": ["a", "b", "c", "c", "d", "e", "f", "g", "g", "g"],
        "Zeroon": [0, 1, 2, 3, 4, 5, 6, 7, 7, 8],
    }
)

# Detecting.
alphabet.duplicated(keep="first")
alphabet.duplicated(keep="first", subset=["Alphabet"])
alphabet.loc[alphabet.duplicated(keep=False, subset=["Alphabet"])]
alphabet.duplicated(keep="first", subset=["Zeroon"])
alphabet.duplicated(keep="last", subset=["Zeroon"])
alphabet.duplicated(keep=False, subset=["Zeroon"])

alphabet[alphabet.duplicated(keep="first")]

# Removing.
alphabet.drop_duplicates()
alphabet.drop_duplicates(subset=["Alphabet"])
alphabet.drop_duplicates(subset=["Zeroon"])
