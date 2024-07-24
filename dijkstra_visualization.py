import matplotlib.pyplot as plt
import networkx as nx
import io

def visualize_graph(graph, shortest_paths=None, start_node=None):
    """
    Візуалізує граф і найкоротші шляхи, знайдені алгоритмом Дейкстри.
    
    :param graph: об'єкт Graph
    :param shortest_paths: словник найкоротших шляхів (за бажанням)
    :param start_node: початкова вершина (за бажанням)
    """
    G = nx.DiGraph()

    for edge, weight in graph.weights.items():
        from_node, to_node = edge
        G.add_edge(from_node, to_node, weight=weight)

    pos = nx.spring_layout(G)  # позиції вершин для візуалізації
    edge_labels = {(u, v): f'{d["weight"]:.2f}' for u, v, d in G.edges(data=True)}

    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=15)

    if shortest_paths and start_node:
        path_edges = []
        for target_node in shortest_paths:
            if target_node != start_node and shortest_paths[target_node] != float('inf'):
                try:
                    path = nx.shortest_path(G, source=start_node, target=target_node, weight='weight')
                    path_edges += list(zip(path[:-1], path[1:]))

                except nx.NetworkXNoPath:
                    continue
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

    plt.title("Graph Visualization with Dijkstra's Shortest Paths")
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return img
