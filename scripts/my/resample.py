import numpy as np
import pandas as pd


rng = pd.date_range("1/1/2012 00:00:05", periods=20, freq="S", name="time")
values = np.random.randint(0, 9, len(rng))
ts = pd.DataFrame(values, index=rng, columns=["value"])
ts.insert(0, "second", ts.index.to_series().apply(lambda x: str(x)[-2:]))
# ts.to_excel('../data/resample.xlsx')
ts_ll = ts.resample("10S", closed="left", label="left")
ts_lr = ts.resample("10S", closed="left", label="right")
ts_rl = ts.resample("10S", closed="right", label="left")
ts_rr = ts.resample("10S", closed="right", label="right")
list(ts_ll)[1]
list(ts_lr)[1]
list(ts_rl)[1]
list(ts_rr)[1]
ts_ll.mean(numeric_only=True)
ts_lr.mean(numeric_only=True)
ts_rl.mean(numeric_only=True)
ts_rr.mean(numeric_only=True)

ts_lls = ts.resample("10S", closed="left", label="left", origin="start")
ts_lls.mean(numeric_only=True)
list(ts_lls)

ts_llo = ts.resample("10S", closed="left", label="left", offset="3S")
ts_llo.mean(numeric_only=True)
list(ts_llo)

ts_llso = ts.resample("10S", closed="left", label="left", origin="start", offset="3S")
ts_llso.mean(numeric_only=True)
list(ts_llso)
