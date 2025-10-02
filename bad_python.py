# bad_script.py

import pandas as pd
import matplotlib.pyplot as plt
import random

data = pd.read_csv("data.csv") # file must exist in same folder

# compute average
avg = 0
for i in range(len(data["value"])):
    avg = avg + data["value"][i]
avg = avg / len(data["value"])
print("average is", avg)

# compute standard deviation (manual way)
sumdiff = 0
for v in data["value"]:
    sumdiff = sumdiff + (v - avg) * (v - avg)
stdev = (sumdiff/len(data["value"]))**0.5
print("std dev is", stdev)

# sample a few rows at random
print("sample rows:")
for i in range(5):
    r = random.randint(0, len(data)-1)
    print(data.iloc[r])

# plot values
plt.plot(data["value"])
plt.title("Values")
plt.show()
