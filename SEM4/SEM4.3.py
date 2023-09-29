import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize = (16,9))
plt1 = fig.add_subplot(211)
plt2 = fig.add_subplot(212)
df = pd.read_csv('iris_data.csv')


a = list(df['Species']).count("Iris-setosa")
b = list(df['Species']).count("Iris-versicolor")
c = list(df['Species']).count("Iris-virginica")

plt1.pie([a, b, c], labels = ['Iris-setosa','Iris-versicolor','Iris-virginica'])

plt1.set_title('Доля видов (Species) ирисов в датасете')

n = list(df['PetalLengthCm'])
df = pd.read_csv('iris_data.csv')
x=[]
y=[]
z=[]
n = list(df['PetalLengthCm'])
for i in range(len(list(df['PetalLengthCm']))):
    if n[i] <= 1.2:
        x.append(n[i])
    elif 1.2 < n[i] <= 1.5:
        y.append(n[i])
    else:
        z.append(n[i])
x = sum(x)
y = sum(y)
z = sum(z)
plt2.pie([x, y, z], labels = ['L<= 1.2','1.2<L<1.5','L>=1.5'])

plt2.set_title('Доли ирисов, у которых длина лепестка (L), см:')

plt.show()
