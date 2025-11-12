import matplotlib.pyplot as plt
import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

titanic["fare"].plot()
titanic["age"].plot()
plt.show()

mean_fare = titanic["fare"].mean()
mean_age = titanic["age"].mean()
std_fare = titanic["fare"].std()
std_age = titanic["age"].std()
# Standardization - calculate how many std separates an observation from the mean?
titanic["fare_z"] = round((titanic["fare"] - mean_fare) / std_fare, 2)
titanic["age_z"] = round((titanic["age"] - mean_age) / std_age, 2)
titanic.head()

titanic["fare_z"].plot()
titanic["age_z"].plot()
plt.show()

# Description shows that data was standardized successfully (mean=0, std=1).
titanic.describe()
