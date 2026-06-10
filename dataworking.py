import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("RESULTS.csv")
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
#start here
#print(df["betting"].unique()) for getting vals
xs=np.array(["full","30p","20p","15p","10p","5p","30","20","15","10","5","ma","card_counting"])
ys=[]
for x in xs:
    value=df[df["betting"]==x]["win_rate[balance]%"].mean()
    ys.append(value)
print(ys)
ys=np.array(ys)
bars=plt.bar(xs,ys,color="limegreen")
adding_numbers(bars)
plt.xlabel("Betting strategies")
plt.ylabel("Average win rate%")
plt.ylim(0,100)
plt.title("Average win rates of each betting type:")
plt.xticks(rotation=45,ha="center")
plt.show()
