import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

pos = 0
scale = 10
size_ax1 = 10000000
size_ax2 = 100000
size_ax3 = 1000
values_ax1 = np.random.normal(pos, scale, size_ax1)
values_ax2 = np.random.normal(pos, scale, size_ax2)
values_ax3 = np.random.normal(pos, scale, size_ax3)

ax1.hist(values_ax1, 100)
ax1.grid()

ax2.hist(values_ax2, 100)
ax2.grid()

ax3.hist(values_ax3, 100)
ax3.grid()
plt.show()