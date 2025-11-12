import numpy as np
import pandas as pd


sales1 = pd.read_csv("data/sales.csv", index_col=0)

sales1.iloc[0, 3] = 23
sales2 = sales1.copy()
sales2.iloc[0, 1], sales2.iloc[2, 2] = 100, 200

# 1st method.
sales1.equals(sales2)

# 2nd method.
sales1 == sales2

# 3rd method.
~(sales1 == sales2)
sales1.where(~(sales1 == sales2))
sales2.where(~(sales1 == sales2))
sales2.where(~(sales1 == sales2)) - sales1.where(~(sales1 == sales2))


# 4th method.
# sales2.rename(columns={'Tue': 'tue'}, inplace=True)  # For column labels equality checking.
# sales2 = sales2.astype({'Thu': 'int'})  # For column dtypes equality checking.


def diff_pd(df1, df2):
    """Identify differences between two pandas DataFrames"""
    assert (df1.columns == df2.columns).all(), print(
        "DataFrame column names are different"
    )
    if any(df1.dtypes != df2.dtypes):
        print("Data Types are different, trying to convert")
        df2 = df2.astype(df1.dtypes)
    if df1.equals(df2):
        return None
    else:
        # need to account for np.nan != np.nan returning True
        diff_mask = (df1 != df2) & ~(df1.isnull() & df2.isnull())
        ne_stacked = diff_mask.stack()
        changed = ne_stacked[ne_stacked]
        changed.index.names = ["id", "col"]
        difference_locations = np.where(diff_mask)
        changed_from = df1.values[difference_locations]
        changed_to = df2.values[difference_locations]
        return pd.DataFrame(
            {"from": changed_from, "to": changed_to}, index=changed.index
        )


print(diff_pd(sales1, sales2))
