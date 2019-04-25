import matplotlib.pyplot as plt
import networkx as nx
import random
#Declaring our Graph class object
Graph = nx.grid_graph(dim=[12,12])
Random_Graph = nx.Graph()
# for i in range(50):
#     Graph.add_node(i)
#     if i >= 1:
#         Graph.add_edge(i, i-1)
#
# for i in range(50):
#     Graph.add_edge(i,random.randint(1,50))


pos = nx.spring_layout(Graph)  # positions for all nodes
# nodes
nx.draw_networkx_nodes(Graph, pos, node_size=100)

# edges
nx.draw_networkx_edges(Graph, pos, width=2)
nx.draw_networkx_edges(Graph, pos, width=2, alpha=0.5, edge_color='cyan', style='dashed')

# labels
nx.draw_networkx_labels(Graph, pos, font_size=11, font_family='sans-serif')

def distance(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
astar_path = nx.astar_path(Graph,(0,0),(random.randint(1,10),random.randint(1, 10)),distance)
print("Generating AStar Path")
print(astar_path)
dijkstra_path = nx.dijkstra_path(Graph,(0,0),(random.randint(1,10),random.randint(1, 10)))
print("Generating dijkstra path")
print(dijkstra_path)

plt.axis('off')
plt.show()


Random_Graph = nx.Graph()
for i in range(50):
    Random_Graph.add_node(i)
    if i >= 1:
        Random_Graph.add_edge(i, i-1)

for i in range(50):
    Random_Graph.add_edge(i,random.randint(1,50))


pos = nx.spring_layout(Random_Graph)  # positions for all nodes
# nodes
nx.draw_networkx_nodes(Random_Graph, pos, node_size=100)

# edges
nx.draw_networkx_edges(Random_Graph, pos, width=2)
nx.draw_networkx_edges(Random_Graph, pos, width=2, alpha=0.5, edge_color='cyan', style='dashed')

# labels
nx.draw_networkx_labels(Random_Graph, pos, font_size=11, font_family='sans-serif')
plt.axis('off')
plt.show()