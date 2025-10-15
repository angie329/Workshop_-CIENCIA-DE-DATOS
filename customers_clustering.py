import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

customers = pd.read_csv('data/Mall_Customers.csv')

sns.set_style('whitegrid')
plt.style.use('fivethirtyeight')
print("Primeras 5 filas del dataset:")
print(customers.head())
print("\nInformación general del dataset:")
customers.info()

print("\nVerificación de valores nulos:")
print(customers.isnull().sum())

#columna 3 y 4 son anual income y spending score
X = customers.iloc[:, [3, 4]].values
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X[:, 0], y=X[:, 1])
plt.title('Clusters de clientes')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()


#METODO DEL CODO
wcss = []
for i in range(1,11):
  kmeans= KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
  kmeans.fit(X) #entrenar al modelo
  wcss.append(kmeans.inertia_)
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('Método del Codo para encontrar el K óptimo')
plt.xlabel('Número de Clusters (K)')
plt.ylabel('WCSS (Inercia)')
plt.xticks(range(1, 11))
plt.show()

#creacion  del modelo k-means final  con 5 clusters
kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=42)

#ajustar modelo y predecir el cluster para cada punto de datos
y_kmeans = kmeans.fit_predict(X) #lista
print("etiqueta dde cluster para los primeros 10 clientes:")
print(y_kmeans[:10])
