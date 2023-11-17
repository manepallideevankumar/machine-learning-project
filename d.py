import random
import pandas as pd
[w1,w2,w3,w4] = [0.815,0.8033,0.8017,0.8065]
vals = []
for i in range(10000):
    x1 = random.randint(4, 7)
    x2 = random.randint(5, 8)
    x3 = random.randint(6 , 9)
    x4 = random.randint(0, 100)
    eq = w1*x1+w2*x2+w3*x3+w4*x4
    vals.append([x1,x2,x3,x4,eq])
df = pd.DataFrame(vals,columns=['data offer','data plan','signal strength','satisfaction','churn'])
df.to_csv('productivity.csv',index=False)