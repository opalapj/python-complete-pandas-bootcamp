import matplotlib.pyplot as plt
import pandas as pd


plt.style.use("seaborn")  # Style selection.

# Detection.
titanic_outliers = pd.read_csv(filepath_or_buffer="data/titanic_outliers.csv")

titanic_outliers.Age.describe()

titanic_outliers.boxplot("Age")
plt.show()

titanic_outliers.Age.plot()
plt.show()

# Replacing.
idx_outl = titanic_outliers.loc[titanic_outliers.Age > 90].index
titanic_outliers.loc[idx_outl, "Age"] = (
    titanic_outliers.loc[titanic_outliers.Age > 90, "Age"] / 10
)
titanic_outliers.loc[idx_outl]
titanic_outliers.loc[217, "Age"] = 42

# Removing.
titanic_outliers.drop(index=217, inplace=True)
