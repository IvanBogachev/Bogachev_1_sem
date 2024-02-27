import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(111)
df = pd.read_csv('BTC_data.csv')
cls = list(df['close'])
tmo = list(df['time'])
tm1 = []
for i in range(len(tmo)):
    a = str(tmo[i])
    tm1.append(a[:10])
ax1.plot(tm1,cls)
x_grad=[]
for i in range(len(df['time'])):
    if i%200 == 0:
        x_grad.append(i)
ax1.grid()
plt.xlabel('DD-MM-YY')
plt.ylabel('Price')
ax1.set_xticks([x_grad[i] for i in range(len(x_grad))])
plt.show()


print(x_grad)