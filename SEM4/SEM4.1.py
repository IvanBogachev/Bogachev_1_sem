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

z1 = np.polyfit(I1,U1,1)
p = np.poly1d(z1)
plt.plot(I1,p(I1))
z2 = np.polyfit(I2,U2,1)
p = np.poly1d(z2)
plt.plot(I2,p(I2) , 'k')
z3 = np.polyfit(I3,U3,1)
p = np.poly1d(z3)
plt.plot(I3,p(I3) , 'g')

plt.scatter(I1, U1, marker='x')
plt.scatter(I2, U2, marker='x')
plt.scatter(I3, U3, marker='x')

plt.grid()

plt.errorbar(I1, U1, yerr=20, xerr =2, color = 'k', linestyle = 'None')
plt.errorbar(I2, U2, yerr=20, xerr =2, color = 'k', linestyle = 'None')
plt.errorbar(I3, U3, yerr=20, xerr =2, color = 'k', linestyle = 'None')
plt.xlabel('I*10^-3,A')
plt.ylabel('U*10^-3,В')
plt.text(0, 750, "Графики для L=20см,L=30см,L=50см", fontsize=10)
plt.show()
