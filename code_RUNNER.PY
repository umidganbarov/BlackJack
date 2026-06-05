import Casino21beta
import pandas as pd
import time

results=[]
initial_balances=[50,100,250,500,1000,5000,10000]
bets=[5,10,15,20,30,"5p","10p","15p","20p","30p","full","ma"]
card_counting=["dont","hilo"]#hilo doesnt cares about initial responces
responces=["random","stand19","stand18","stand17","stand16","stand15","stand14"]
x=0
for i in range( 15000):
    x=i+x
start=time.time()
shoes=26000
c = 0
total = len(initial_balances) * len(bets) * len(card_counting) * len(responces)

for ibalance in initial_balances:
    for bet in bets:
        for counting in card_counting:
            for resp in responces:
                data=Casino21beta.Main(shoes,ibalance,bet,counting,resp)
                results.append(data)
                c+=1
                if c % (total // 100) == 0:
                    print(f"{c*100//total}%", flush=True)
df=pd.DataFrame(results)
df.to_csv("RESULTS.csv",index=False)
end=time.time()

print(df)
print(f"Times: {shoes}\nTime[sec]: {(end-start):.3f}")
print("DONE!")
