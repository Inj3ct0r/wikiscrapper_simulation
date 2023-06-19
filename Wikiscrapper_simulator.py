import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd

# Simulador Wikiscrapper con 'n' número de iteraciones

# Número de nodos de cada camino
epochs = 20
# Número de caminos generados a partir del Wikiscrapper
paths = 20
# Simulamos un universo de links ya conocidos representados como números
num_links = 200
universe = list(range(num_links))
"""
El problema de usar un universo conocido es que aumenta demasiado la probabilidad de obtener los mismos links en distintos caminos
La dificultad está en trabajar con un algoritmo que funciona en base a decisiones aleatorias
"""

# Creamos un Digrafo vacío
G = nx.DiGraph()
# Definimos una variable que guarda el link de partida
initial_link = 0
# Definimos una variable que guarda el ultimo link visitado
last_link = 0

# Simulamos el Wikiscrapper 'n' número de veces a partir de un mismo link inicial
for i in range(1,paths+1):
    # Simulamos un camino con 'k' nodos (epochs)
    links = random.choices(universe, k=epochs)
    # Insertamos el link inicial en la primera posición para forzar que cada camino provenga de este
    links.insert(0, initial_link)
    print("Lista número %g" %i, links)
    # Conectamos cada nodo del camino recorrido
    for link in links:
        G.add_edge(last_link, link)
        last_link = link
    # Refrescamos el valor del ultimo link visitado al del link inicial
    last_link = 0

# Ploteamos
fig, ax = plt.subplots(figsize = (10,5))
node_list=[]
value_list=[]
# Obtenemos los grados de cada nodo
for node in G.nodes():
    d = G.degree(node)
    node_list.append("Nodo"+str(node))
    value_list.append(d)
    #print(node,d)


# Eliminamos los loops (Puede que se tenga que sacar)
G.remove_edges_from(nx.selfloop_edges(G))
# Definimos el tipo de grafo
pos = nx.circular_layout(G)
# Colocamos el nodo inicial al medio
pos[0] = np.array([0, 0])
# Parámetros del grafo
nx.draw(G, pos=pos, node_size=40)
nx.degree_centrality(G)
plt.show()

if value_list[0]>2:
    value_list[0]=value_list[0]-2 #corección del nodo 0, el histograma siempre arroja 2 valores adicionales que "no existen"

diccionario={"Nodos":node_list,"Grados":value_list}
df= pd.DataFrame(diccionario)
df.sort_values(by=['Grados'], inplace=True)

plt.bar(df["Nodos"],df["Grados"], color = "cyan", ec="white")
plt.xlabel("Nodos")
plt.ylabel("Valor del grado del nodo")
plt.xticks(rotation=90)
plt.show()