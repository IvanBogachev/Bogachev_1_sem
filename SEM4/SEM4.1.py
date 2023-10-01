import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize = (16,9))
df = pd.read_csv('Laba_fiz.csv')
I1 = list(df['1I*10^-3'])
U1 = list(df['1U*10^-3'])
I2 = list(df['2I*10^-3'])
U2 = list(df['2U*10^-3'])
I3 = list(df['3I*10^-3'])
U3 = list(df['3U*10^-3'])
x = [0, 300 ]
l20 = np.interp(x, I1, U1)
l30 = np.interp(x, I2, U2)
l50 = np.interp(x, I3, U3)

plt.plot(x,l20, 'r')
plt.plot(x,l30, 'b')
plt.plot(x,l50, 'k')
plt.grid()U*10^-3

plt.xlabel('I*10^-3')
plt.ylabel('U*10^-3')
plt.show()