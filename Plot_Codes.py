I am including codes here as TEST 1, 2, 3... numbers and parts a, b, c... etc.
For all codes note that
---------------------------------------------------
def adding_numbers(bars):
    for bar in bars:
        height = bar.get_height()
        plt.text(
        bar.get_x() + bar.get_width()/2,
        height+2,
        f"{height:.1f}%",
        ha='center',
        color="black"
        )
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("RESULTS.csv")
---------------------------------------------------
TEST1:
df_counted= df[df["card_counting"]!="dont"]
df_dont=df[df["card_counting"]=="dont"]
print(df_counted[["win_rate[balance]%"]].mean())
print(df_dont[["win_rate[balance]%"]].mean())

TEST2:
A]
