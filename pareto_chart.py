import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

df = pd.DataFrame({'xChar': [104, 42, 20, 16, 8, 7, 3]})
df.index = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
df = df.sort_values(by='xChar',ascending=False)
df["cumpercentage"] = df["xChar"].cumsum()/df["xChar"].sum()*100
percentList = df["cumpercentage"].tolist()
percentList.insert(0, 0)
print(percentList)

barWidth = 1

fig, ax = plt.subplots()
ax.bar(df.index, df["xChar"], color="C0", width=barWidth)
ax2 = ax.twinx()
ax2.plot([idx - barWidth / 2 for idx in np.arange(len(percentList))], percentList, color="C1", marker="D", ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())

ax.set_ylim(ymax=df["xChar"].sum())
ax.tick_params(axis="y", colors="C0")
ax.set_xlim(xmin=-1 * barWidth / 2, xmax=len(df.index) - barWidth / 2)
ax2.set_ylim(ymin=0, ymax=100)
ax2.tick_params(axis="y", colors="C1")

plt.show()