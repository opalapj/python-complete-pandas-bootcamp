import numpy as np
import pandas as pd
import pandas.tseries.offsets as offset


# Helpful function.
def attributes(sampler):
    print("closed:", sampler.closed)
    print("label:", sampler.label)
    print("origin:", sampler.origin)


# Input data in 15-minute intervals.
rng = pd.date_range(
    start="2023-01-01", end="2025-01-01", freq="5T", tz="Poland", inclusive="left"
)
values = np.random.randint(0, 100, len(rng))
ts = pd.DataFrame(values, index=rng, columns=["value"])

# Hourly resampling.
# Each hour begins at zero minutes 00:00. (default timestamp for sampling)
ts_h = ts.resample(rule="H")
ts_h = ts.resample(rule="H", closed="right", label="right")
attributes(ts_h)
ts_h.ohlc()
ts_h.count().value_counts()
list(ts_h)[0]
list(ts_h)[1]

# Daily sampling.
# Each day begins at midnight 00:00:00. (default timestamp for sampling)
ts_d = ts.resample(rule="D")
ts_d = ts.resample(rule="D", closed="right", label="right")
attributes(ts_d)
ts_d.ohlc()
ts_d.count().value_counts()
list(ts_d)[0]
list(ts_d)[1]

# Weekly sampling.
# Each week ends on Sunday weekday=6. (default timestamp for sampling)
ts_w = ts.resample(rule="W")
# But, it could be more suitable to take a week beginning as timestamp and label.
ts_w = ts.resample(rule=offset.Week(weekday=0), closed="left", label="left")
# ts_w1 = ts.resample(rule='W-Wed')
# ts_w2 = ts.resample(rule=pd.tseries.offsets.Week(weekday=2))  # The same result.
attributes(ts_w)
ts_w.ohlc()
ts_w.count().value_counts()
list(ts_w)[0]
list(ts_w)[1]

# Monthly sampling.
# Each month ends on the last day of month (only date, without time). (default timestamp for sampling)
ts_m = ts.resample(rule="M")
ts_m = ts.resample(
    rule="M", closed="left"
)  # it is evident with closed='left' parameter.
# But, it could be more suitable to take a month beginning as timestamp and label.
ts_m = ts.resample(rule=offset.MonthBegin())
ts_m = ts.resample(rule="MS")  # The same result with shorter alias.
attributes(ts_m)
ts_m.ohlc()
ts_m.count().value_counts()
list(ts_m)[0]
list(ts_m)[1]

# Quarterly sampling.
# Each quarter ends on the last day of quarter (only date, without time). (default timestamp for sampling)
ts_q = ts.resample(rule="Q")
ts_q = ts.resample(
    rule="Q", closed="left"
)  # it is evident with closed='left' parameter.
# But, it could be more suitable to take a quarter beginning as timestamp and label.
ts_q = ts.resample(rule=offset.QuarterBegin(startingMonth=1))
ts_q = ts.resample(rule="QS")  # The same result with shorter alias.
attributes(ts_q)
ts_q.ohlc()
ts_q.count().value_counts()
list(ts_q)[0]
list(ts_q)[1]

# Annual sampling.
# Each year ends on the last day of year (only date, without time). (default timestamp for sampling)
ts_a = ts.resample(rule="A")
ts_a = ts.resample(
    rule="A", closed="left"
)  # it is evident with closed='left' parameter.
# But, it could be more suitable to take a year beginning as timestamp and label.
ts_a = ts.resample(rule=offset.YearBegin())
ts_a = ts.resample(rule="AS")  # The same result with shorter alias.
attributes(ts_a)
ts_a.ohlc()
ts_a.count().value_counts()
list(ts_a)[0]
list(ts_a)[1]
