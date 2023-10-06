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
x1 = [0, 141]
x2 = [0, 236]
x3 = [0, 258]
l20 = np.interp(x1, I1, U1)
l30 = np.interp(x2, I2, U2)
l50 = np.interp(x3, I3, U3)

plt.scatter(I1, U1, marker='x')
plt.scatter(I2, U2, marker='x')
plt.scatter(I3, U3, marker='x')

plt.plot(x1, l20, 'b')
plt.plot(x2, l30, 'y')
plt.plot(x3, l50, 'g')

plt.grid()

plt.errorbar(I1, U1, yerr=20, xerr =2, color = 'k', linestyle = 'None')
plt.errorbar(I2, U2, yerr=20, xerr =2, color = 'k', linestyle = 'None')
plt.errorbar(I3, U3, yerr=20, xerr =2, color = 'k', linestyle = 'None')
plt.xlabel('I*10^-3,A')
plt.ylabel('U*10^-3,В')
plt.show()
# politlib с параметром 1