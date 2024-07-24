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
    """
    G, pos = build_graph(tree_root)
    visited = set()
    stack = [tree_root]
    traversal_order = []

    while stack:
        node = stack.pop()
        if node.id not in visited:
            visited.add(node.id)
            traversal_order.append(node.id)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    colors = get_colors(len(traversal_order))
    node_colors = {node_id: color for node_id, color in zip(traversal_order, colors)}
    node_labels = {node[0]: node[1]['label'] for node in G.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(G, pos=pos, with_labels=True, labels=node_labels, node_color=[node_colors[node] for node in G.nodes()], node_size=2500, arrows=False)
    plt.title("DFS Traversal")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return img

def visualize_bfs(tree_root):
    """
    Візуалізує обхід дерева в ширину (BFS) за допомогою matplotlib.
    
    :param tree_root: корінь дерева
    """
    G, pos = build_graph(tree_root)
    visited = set()
    queue = [tree_root]
    traversal_order = []

    while queue:
        node = queue.pop(0)
        if node.id not in visited:
            visited.add(node.id)
            traversal_order.append(node.id)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    colors = get_colors(len(traversal_order))
    node_colors = {node_id: color for node_id, color in zip(traversal_order, colors)}
    node_labels = {node[0]: node[1]['label'] for node in G.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(G, pos=pos, with_labels=True, labels=node_labels, node_color=[node_colors[node] for node in G.nodes()], node_size=2500, arrows=False)
    plt.title("BFS Traversal")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return img

def build_graph(tree_root):
    G = nx.DiGraph()
    pos = {}
    def add_edges(node, x=0, y=0, layer=1):
        if node is not None:
            G.add_node(node.id, label=node.val)
            pos[node.id] = (x, y)
            if node.left:
                G.add_edge(node.id, node.left.id)
                add_edges(node.left, x - 1 / 2 ** layer, y - 1, layer + 1)
            if node.right:
                G.add_edge(node.id, node.right.id)
                add_edges(node.right, x + 1 / 2 ** layer, y - 1, layer + 1)
    add_edges(tree_root)
    return G, pos
