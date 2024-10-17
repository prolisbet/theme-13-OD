import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)

    return root


def add_edges(graph, root, pos=None, x=0, y=0, layer=1):
    if root is not None:
        graph.add_node(root.value, pos=(x, y))
        if root.left is not None:
            graph.add_edge(root.value, root.left.value)
            l = x - 1 / 2 ** layer
            add_edges(graph, root.left, x=l, y=y-1, layer=layer+1)
        if root.right is not None:
            graph.add_edge(root.value, root.right.value)
            r = x + 1 / 2 ** layer
            add_edges(graph, root.right, x=r, y=y-1, layer=layer+1)


def draw_tree(root):
    graph = nx.DiGraph()
    add_edges(graph, root)
    pos = nx.get_node_attributes(graph, 'pos')
    nx.draw(graph, pos, with_labels=True, arrows=False, node_size=2000, node_color='lightblue')
    plt.show()


root = Node(70)

root = insert(root, 30)
root = insert(root, 56)
root = insert(root, 89)
root = insert(root, 45)
root = insert(root, 60)
root = insert(root, 73)
root = insert(root, 98)
root = insert(root, 84)

draw_tree(root)
