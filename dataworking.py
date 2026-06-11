def adding_numbers(bars):
    for bar in bars:
        height = bar.get_height()
        plt.text(
        bar.get_x() + bar.get_width()/2,
        height+2,
        f"{height:.1f}%",
        ha='center',
        color="navy"#,weight="semi"
        )
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("RESULTS.csv")
df["max_balance%"]=df["max_balance"]/df["initial_balance"]*100
df["loses%"]=df["losses[num]"]/df["total_hands"]*100
#start here
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
df7=df.sort_values(by="loses%",ascending=False)[["loses%","strategy","betting","card_counting","initial_balance","median","win_rate[balance]%"]].head(10)
fig,ax= plt.subplots()
ax.axis('off')
df7["loses%"]=df7["loses%"].map(lambda x:f"{x:.1f}%")
df7["win_rate[balance]%"]=df7["win_rate[balance]%"].map(lambda x:f"{x:.1f}%")


table=ax.table(cellText=df7.values,colLabels=df7.columns,loc="center",cellLoc="center",colColours=["#FF3300"] * len(df7.columns)  )
table.scale(1.3,2)


plt.title("Top 10 highest number of loses")
plt.show()

