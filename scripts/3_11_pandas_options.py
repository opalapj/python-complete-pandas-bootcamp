# https://pandas.pydata.org/docs/user_guide/options.html#

import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

titanic.head()
titanic.head(20)

titanic.tail()
titanic.tail(20)

pd.describe_option()

pd.describe_option("display.min_rows", True)

pd.get_option("display.min_rows")
# Alternative way of getting.
pd.options.display.min_rows

pd.set_option("display.min_rows", 5)
# Alternative way of setting.
pd.options.display.min_rows = 5

pd.reset_option("display.min_rows")

# If max greater than df display whole df.
pd.set_option("display.max_rows", 10)
pd.reset_option("display.max_rows")

# If min is None display max_rows of df.
pd.set_option("display.min_rows", None)
pd.reset_option("display.min_rows")

pd.set_option("display.width", None)
# Reset all options with 'display' prefix.
pd.reset_option("display")

# Context manager to temporarily set options in the with statement context.
with pd.option_context("display.max_rows", 10, "display.max_columns", 5):
    print(titanic.head(20))
