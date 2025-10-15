# Workshop_-CIENCIA-DE-DATOS

# 🚀 Clustering de Clientes con K-Means – Proyecto de Ciencia de Datos

¡Bienvenido a mi proyecto de **segmentación de clientes**! 😃  
En este repositorio aplicamos **Machine Learning no supervisado** para entender mejor a los clientes de un mall, utilizando **K-Means** para agruparlos según su **ingreso anual** y su **puntuación de gasto**.  

Este proyecto no solo es un ejercicio de programación y análisis de datos, ¡sino también una exploración real de cómo podemos usar la ciencia de datos para **tomar decisiones de negocio inteligentes**! 

---

## 💡 Objetivo del Proyecto

El objetivo principal es **clasificar clientes en diferentes grupos** según sus patrones de gasto y nivel de ingresos. Esto permite:  

- Identificar clientes premium que merecen ofertas exclusivas.  
- Detectar clientes impulsivos o jóvenes que buscan tendencias.  
- Encontrar segmentos que requieren estrategias de marketing masivo o fidelización.  
- Crear un **mapa visual de comportamiento del consumidor** para futuras decisiones comerciales.  

---

## 📂 Estructura del Proyecto

Workshop_-CIENCIA-DE-DATOS/
├── data/
│ └── Mall_Customers.csv # Dataset con información de clientes
├── src/
│ └── customers_clustering.py # Script principal con análisis y modelo
├── requirements.txt # Librerías necesarias para ejecutar el proyecto
├── README.md # Este archivo
└── .gitignore # Archivos ignorados por Git



## 🧰 Tecnologías y Librerías Utilizadas

- **Python 3.8+** – lenguaje principal de programación  
- [pandas](https://pandas.pydata.org/) – manejo y limpieza de datos  
- [numpy](https://numpy.org/) – operaciones matemáticas y arrays  
- [matplotlib](https://matplotlib.org/) – visualización de datos  
- [seaborn](https://seaborn.pydata.org/) – gráficos estadísticos y estéticos  
- [scikit-learn](https://scikit-learn.org/stable/) – algoritmo K-Means  
- **Git & GitHub** – control de versiones y colaboración  

---

## 🎯 Flujo del Proyecto

1. **Carga y exploración del dataset**  
   - Revisión de las primeras filas y estructura general.  
   - Verificación de valores nulos y tipos de variables.  

2. **Visualización inicial de datos**  
   - Scatter plot de ingresos vs. puntuación de gasto.  
   - Estilo gráfico profesional usando `seaborn` y `matplotlib`.  

3. **Determinación del número óptimo de clusters**  
   - Uso del **Método del Codo (Elbow Method)**.  
   - Evaluación de la inercia (WCSS) para elegir el valor de K.  

4. **Entrenamiento del modelo K-Means**  
   - Ajuste del modelo con K clusters (K=5 recomendado).  
   - Predicción del cluster para cada cliente.  

5. **Visualización final de los clusters**  
   - Scatter plot por cluster, con centroides en amarillo.  
   - Colores y etiquetas claras para fácil interpretación.  

6. **Interpretación de los clusters y estrategias**  
   - Cada cluster se analiza para comprender patrones de comportamiento.  
   - Se sugieren estrategias de marketing y fidelización basadas en los grupos.

---

## 🧩 Interpretación de los Clusters

| Cluster | Descripción | Estrategia sugerida |
|---------|-------------|-------------------|
| 🟥 Rojo | Clientes con ingresos medios y gasto medio | Marketing masivo, promociones generales |
| 🟦 Azul | Clientes con ingresos altos y alto gasto | Ofertas exclusivas y productos premium |
| 🟩 Verde | Jóvenes impulsivos y derrochadores | Productos de moda, tendencias y novedades |
| 🟪 Violeta | Ahorradores, bajo gasto | Productos duraderos y programas de fidelización |
| 🟦 Celeste | Clientes que visitan poco o no compran mucho | Incentivos, descuentos y campañas de retención |

💡 Este análisis permite **tomar decisiones de marketing más inteligentes**, diseñar campañas personalizadas y mejorar la experiencia del cliente.

---

## 🚀 Cómo Ejecutar el Proyecto

1. **Clonar el repositorio**
```bash
git clone https://github.com/tuusuario/Workshop_-CIENCIA-DE-DATOS.git
cd Workshop_-CIENCIA-DE-DATOS