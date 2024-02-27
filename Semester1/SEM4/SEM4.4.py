import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize = (20,30))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

df = pd.read_csv('iris_data.csv')
sep_len = list(df['SepalLengthCm'])
sep_wid = list(df['SepalWidthCm'])
pet_len = list(df['PetalLengthCm'])
pet_wid = list(df['PetalWidthCm'])

ax1.scatter(sep_len, sep_wid, marker='.')
ax2.scatter(sep_len, pet_len, marker='.')
ax3.scatter(sep_len, pet_wid, marker='.')

plt.show()
fig = plt.figure(figsize = (20,30))

df = pd.read_csv('iris_data.csv')
sep_len = list(df['SepalLengthCm'])
sep_wid = list(df['SepalWidthCm'])
pet_len = list(df['PetalLengthCm'])
pet_wid = list(df['PetalWidthCm'])

ax4 = fig.add_subplot(311)
ax5 = fig.add_subplot(312)
ax6 = fig.add_subplot(313)
ax4.scatter(sep_wid, pet_len, marker='.')
ax5.scatter(sep_wid, pet_wid, marker='.')
ax6.scatter(pet_len, pet_wid, marker='.')
plt.show()
# Наиболее похож на прямую график 6
fig = plt.figure(figsize = (20,30))

df = pd.read_csv('iris_data.csv')
pet_len = list(df['PetalLengthCm'])
pet_wid = list(df['PetalWidthCm'])
ax6 = fig.add_subplot(111)
ax6.scatter(pet_len, pet_wid, marker='.')

z = np.polyfit(pet_len ,pet_wid,1)
p = np.poly1d(z)
ax6.plot(pet_len,p(pet_len) , 'k')
plt.grid()
plt.xlabel('PetalLengthCm')
plt.ylabel('PetalWidthCm')
print("Коэффициенты линии МНК" , z)
plt.show()
