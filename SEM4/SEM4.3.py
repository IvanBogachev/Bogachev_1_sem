import matplotlib.pyplot as plt
import pandas as pd
fig = plt.figure(figsize = (16,9))
plt1 = fig.add_subplot(211)
plt2 = fig.add_subplot(212)
df = pd.read_csv('iris_data.csv')

setosa = list(df['Species']).count("Iris-setosa")
versicolor = list(df['Species']).count("Iris-versicolor")
virginica = list(df['Species']).count("Iris-virginica")

plt1.pie([setosa, versicolor, virginica], labels = ['Iris-setosa','Iris-versicolor','Iris-virginica'])

plt1.set_title('Доля видов (Species) ирисов в датасете')


df = pd.read_csv('iris_data.csv')
short=[]
medium=[]
long=[]
for i in range(len(list(df['PetalLengthCm']))):
    if list(df['PetalLengthCm'])[i] <= 1.2:
        short.append(list(df['PetalLengthCm'])[i])
    elif 1.2 < list(df['PetalLengthCm'])[i] <= 1.5:
        medium.append(list(df['PetalLengthCm'])[i])
    else:
        long.append(list(df['PetalLengthCm'])[i])
short = sum(short)
medium = sum(medium)
long = sum(long)
plt2.pie([short, medium, long], labels = ['L <=1.2','1.2< L <1.5','L >=1.5'])

plt2.set_title('Доли ирисов, у которых длина лепестка, L [см] :')

plt.show()
