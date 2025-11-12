import matplotlib.pyplot as plt
import pandas as pd


temp = pd.read_csv("data/temp.csv", parse_dates=True, index_col="datetime")

temp.info()
temp.describe()

plt.isinteractive()
plt.ion()

# 1st way to create subplots.
# Figure could be even better prepared e.g. colors, ticks, legend, cursor coordinates.
temp.plot(subplots=True, layout=(2, 1))

# 2nd way to create subplots.
fig, ax = plt.subplots(2, 1, sharex=True)
ax[0].plot(temp["LA"])
ax[1].plot(temp["NY"])
