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
