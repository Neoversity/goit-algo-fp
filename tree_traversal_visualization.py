import networkx as nx
import matplotlib.pyplot as plt
import io
import numpy as np
import matplotlib.colors as mcolors


def get_colors(num_colors):
    """
    Генерує кольорову шкалу від темного до світлого.

    :param num_colors: кількість кольорів
    :return: список кольорів
    """
    colors = plt.cm.viridis_r(np.linspace(0, 1, num_colors))
    return [mcolors.to_hex(c) for c in colors]


def visualize_dfs(tree_root):
    """
    Візуалізує обхід дерева в глибину (DFS) за допомогою matplotlib.

    :param tree_root: корінь дерева
    :return: зображення у форматі BytesIO
    """
    G, pos = build_graph(tree_root)
    visited = set()  # Множина для відстеження відвіданих вузлів
    stack = [tree_root]  # Стек для обходу в глибину
    traversal_order = []  # Порядок обходу вузлів

    while stack:
        node = stack.pop()  # Витягуємо вузол зі стеку
        if node.id not in visited:
            visited.add(node.id)
            traversal_order.append(node.id)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    # Генеруємо кольори для кожного вузла в порядку обходу
    colors = get_colors(len(traversal_order))
    node_colors = {node_id: color for node_id, color in zip(traversal_order, colors)}
    node_labels = {node[0]: node[1]["label"] for node in G.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        G,
        pos=pos,
        with_labels=True,
        labels=node_labels,
        node_color=[node_colors[node] for node in G.nodes()],
        node_size=2500,
        arrows=False,
    )
    plt.title("DFS Traversal")

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plt.close()
    return img


def visualize_bfs(tree_root):
    """
    Візуалізує обхід дерева в ширину (BFS) за допомогою matplotlib.

    :param tree_root: корінь дерева
    :return: зображення у форматі BytesIO
    """
    G, pos = build_graph(tree_root)
    visited = set()  # Множина для відстеження відвіданих вузлів
    queue = [tree_root]  # Черга для обходу в ширину
    traversal_order = []  # Порядок обходу вузлів

    while queue:
        node = queue.pop(0)  # Витягуємо вузол з черги
        if node.id not in visited:
            visited.add(node.id)
            traversal_order.append(node.id)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # Генеруємо кольори для кожного вузла в порядку обходу
    colors = get_colors(len(traversal_order))
    node_colors = {node_id: color for node_id, color in zip(traversal_order, colors)}
    node_labels = {node[0]: node[1]["label"] for node in G.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        G,
        pos=pos,
        with_labels=True,
        labels=node_labels,
        node_color=[node_colors[node] for node in G.nodes()],
        node_size=2500,
        arrows=False,
    )
    plt.title("BFS Traversal")

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plt.close()
    return img


def build_graph(tree_root):
    """
    Створює граф з дерева.

    :param tree_root: корінь дерева
    :return: об'єкт графа і позиції вузлів
    """
    G = nx.DiGraph()
    pos = {}

    def add_edges(node, x=0, y=0, layer=1):
        if node is not None:
            G.add_node(node.id, label=node.val)
            pos[node.id] = (x, y)
            if node.left:
                G.add_edge(node.id, node.left.id)
                add_edges(node.left, x - 1 / 2**layer, y - 1, layer + 1)
            if node.right:
                G.add_edge(node.id, node.right.id)
                add_edges(node.right, x + 1 / 2**layer, y - 1, layer + 1)

    add_edges(tree_root)
    return G, pos
