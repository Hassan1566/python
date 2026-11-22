import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

#sns.relplot(data=df, x="total_bill", y="tip", hue="size", palette="ch:start=.2,rot=-.3", size="size",
            #sizes=(15,200), alpha=.5, linewidth=.5, edgecolor="white")

dowjones = sns.load_dataset("dowjones")
print(dowjones.head())

plt.show()

