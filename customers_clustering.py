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


# GRAFICO DE DISPERSION
plt.figure(figsize=(12,8))

#graficar los puntos de cada cluster con un color diferente
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=60, c='red', label='Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=60, c='blue', label='Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=60, c='green', label='Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s=60, c='violet', label='Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s=60, c='cyan', label='Cluster 5')

#graficar los centroides:
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='yellow', label='Centroides')
plt.title('Clusters de clientes')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

"""cluser(rojo) = ingresos medios y puntuación de gasto medio, programas de marketing masivo

cluster(azul) = "objetivo premium"

cluster(verde) = "impulsivos, jovenes derrochadores", jovenes receptivos a tendencias, moda rapida, productos novedosos

cluster(violeta) = ahorradores, ofrecer productos duraderos

cluster(celeste) = clientes que visitan poco o no encuentran productos a su alcance
"""