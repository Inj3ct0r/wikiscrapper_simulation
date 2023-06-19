import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd

# Wikiscrapper simulator with 'n' number of iterations over a single element

# Number of nodes of each path
epochs = 4
# Number of iterations (paths) of the simulation
paths = 4
# We simulate a universe of values that tries to mimics the amount of available links found by the crawler
num_links = 100
universe = list(range(num_links))
"""
Using a known universe of values to visit implies that visiting the same element is a probabilistic event rather than
a random occurence
"""

# Create empty Digraph
G = nx.DiGraph()
# Save the initial element
initial_link = 0
# Save the last visited element
last_link = 0

# The Wikiscrapper simulator
for i in range(1,paths+1):
    # Simulate a path with 'k' nodes (epochs)
    links = random.choices(universe, k=epochs)
    # Assign the initial element as the first position to force each path to start from it
    links.insert(0, initial_link)
    print("List %g" %i, links)
    # Add edges to all the nodes in the path
    for link in links:
        G.add_edge(last_link, link)
        last_link = link
    # Refresh the last visited element for next iteration
    last_link = 0

# Plot section
fig, ax = plt.subplots(figsize = (10,5))

node_list=[]
degree_list=[]

# Get the degree of each node
for node in G.nodes():
    d = G.degree(node)
    node_list.append("Node "+str(node))
    degree_list.append(d)
    #print(node,d)


# Remove node loops
G.remove_edges_from(nx.selfloop_edges(G))
# Plot as small-world network
pos = nx.circular_layout(G)
# Set first element position to the center of the figure
pos[0] = np.array([0, 0])
# Graph draw parameters
nx.draw(G, pos=pos, node_size=40)
plt.show()

# The initial element will always have 2 more degrees because it creates an edge pointing to itself on initial iteration so we substract them
if degree_list[0]>2:
    degree_list[0]=degree_list[0]-2

# Create a sorted bar plot of the degree of each node
dict = {"Nodes": node_list, "Degrees": degree_list}
df = pd.DataFrame(dict)
df.sort_values(by=['Degrees'], inplace=True)

plt.bar(df["Nodes"],df["Degrees"], color = "#035efc", ec="black")
plt.xlabel("Nodes")
plt.ylabel("Weights")
plt.title("Distribution of degrees")
plt.xticks(rotation=45)
plt.show()