import numpy as np
import pandas as pd

dataset = pd.read_csv("data/BSS_hour_raw.csv").copy()

ds2 = np.random.permutation(dataset)
headers = ["dteday", "season", "hour", "holiday", "weekday", "workingday", "weather", "temp", "atemp", "hum",
           "windspeed", "casual", "registered"]
# train = ds2[:int(len(ds2) / 2)]
# test = ds2[int(len(ds2) / 2):]
train = ds2[:100]
test = ds2[-100:]

train = np.insert(train, 0, headers, axis=0)
test = np.insert(test, 0, headers, axis=0)

pd.DataFrame(train).to_csv("data/BSS_hour_raw copy.csv", header=None, index=None)
pd.DataFrame(test).to_csv("data/BSS_hour_raw copy 2.csv", header=None, index=None)
