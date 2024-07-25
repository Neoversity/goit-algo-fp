import uuid
import networkx as nx
import matplotlib.pyplot as plt
import io

class Node:
    """
    Клас, що представляє вузол дерева.
    """
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def array_to_heap(arr):
    """
    Перетворює масив на дерево-купу.
    
    :param arr: вхідний масив
    :return: корінь дерева-купи
    """
    if not arr:
        return None

    # Створення вузлів для кожного елемента масиву
    nodes = [Node(key) for key in arr]
    
    # Призначення лівих і правих дочірніх вузлів
    for i in range(len(nodes)):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]

    return nodes[0]

def draw_heap_tree(tree_root):
    """
    Малює дерево-купу за допомогою matplotlib і networkx.
    
    :param tree_root: корінь дерева-купи
    :return: зображення у форматі BytesIO
    """
    G, pos = build_graph(tree_root)
    colors = [node[1]['color'] for node in G.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in G.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, labels=labels, node_size=2500, node_color=colors, with_labels=True)
    plt.title("Heap Visualization")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return img

def build_graph(tree_root):
    """
    Створює граф з дерева-купи.
    
    :param tree_root: корінь дерева-купи
    :return: об'єкт графа і позиції вузлів
    """
    G = nx.DiGraph()
    pos = {}

    def add_edges(node, x=0, y=0, layer=1):
        if node is not None:
            G.add_node(node.id, color=node.color, label=node.val)
            pos[node.id] = (x, y)
            if node.left:
                G.add_edge(node.id, node.left.id)
                add_edges(node.left, x - 1 / 2 ** layer, y - 1, layer + 1)
            if node.right:
                G.add_edge(node.id, node.right.id)
                add_edges(node.right, x + 1 / 2 ** layer, y - 1, layer + 1)
    
    add_edges(tree_root)
    return G, pos

def is_valid_heap(heap_root):
    """
    Перевіряє, чи дотримується властивості мін-купи для дерева.
    
    :param heap_root: корінь дерева купи
    :return: True, якщо дотримується, False в іншому випадку
    """
    def is_valid(node):
        if not node:
            return True
        if node.left and node.val > node.left.val:
            return False
        if node.right and node.val > node.right.val:
            return False
        return is_valid(node.left) and is_valid(node.right)
    
    return is_valid(heap_root)
