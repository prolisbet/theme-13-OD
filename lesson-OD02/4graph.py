import matplotlib.pyplot as plt
import networkx as nx


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))


graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.print_graph()

# Визуализация графа
G = nx.DiGraph()

for node, edges in graph.graph.items():
    for edge in edges:
        G.add_edge(node, edge)

pos = nx.spring_layout(G)  # Расположение узлов
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold',
        arrowsize=20)
plt.show()
