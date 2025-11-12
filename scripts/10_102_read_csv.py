import pandas as pd


titanic = pd.read_csv(
    filepath_or_buffer="data/titanic.csv",
    # index_col='pclass',
    # index_col='3',
    # header=1
    # header=0,
    # names=[chr(i) for i in range(ord('a'), ord('a')+9)],
    # usecols=[1, 3, 5]
    usecols=["survived", "pclass", "sex", "age"],
    index_col="pclass",
)

titanic.columns = ["alive", "gender", "age"]
titanic.index.name = "class"

titanic.head()
