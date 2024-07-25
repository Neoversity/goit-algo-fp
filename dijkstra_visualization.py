import random
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import io


class Graph:
    """
    Клас для представлення графа.
    """

    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        """
        Додає ребро до графа.

        :param from_node: початкова вершина
        :param to_node: кінцева вершина
        :param weight: вага ребра
        """
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[to_node].append((from_node, weight))

    def draw_graph_with_paths(self, shortest_paths, start_node):
        """
        Малює граф з коротшими шляхами.

        :param shortest_paths: коротші шляхи від стартової вершини
        :param start_node: стартова вершина
        """
        G = nx.Graph()
        for from_node, edges in self.edges.items():
            for to_node, weight in edges:
                G.add_edge(from_node, to_node, weight=weight)

        pos = nx.spring_layout(G)
        plt.figure()
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="skyblue",
            node_size=3000,
            font_size=18,
            font_weight="bold",
        )
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=14)

        for node, distance in shortest_paths.items():
            if node != start_node:
                path = nx.shortest_path(
                    G, source=start_node, target=node, weight="weight"
                )
                path_edges = list(zip(path, path[1:]))
                nx.draw_networkx_edges(
                    G, pos, edgelist=path_edges, edge_color="r", width=2
                )

        img = io.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        plt.close()
        return img


def generate_connected_random_graph(num_nodes, num_edges):
    """
    Генерує зв'язаний випадковий граф.

    :param num_nodes: кількість вершин
    :param num_edges: кількість ребер
    :return: об'єкт графа
    """
    if num_nodes < 2:
        raise ValueError("Number of nodes must be at least 2.")
    if num_edges < num_nodes - 1:
        raise ValueError(
            "Number of edges must be at least number of nodes minus one for a connected graph."
        )
    if num_edges > num_nodes * (num_nodes - 1) / 2:
        raise ValueError("Too many edges for the given number of nodes.")
    graph = Graph()
    edges_set = set()
    while len(edges_set) < num_edges:
        from_node = str(random.randint(1, num_nodes))
        to_node = str(random.randint(1, num_nodes))
        if (
            from_node != to_node
            and (from_node, to_node) not in edges_set
            and (to_node, from_node) not in edges_set
        ):
            weight = round(random.uniform(1, 10), 2)
            graph.add_edge(from_node, to_node, weight)
            edges_set.add((from_node, to_node))
    return graph


def dijkstra(graph, start):
    """
    Алгоритм Дейкстри для знаходження найкоротших шляхів у графі.

    :param graph: об'єкт графа
    :param start: стартова вершина
    :return: словник з найкоротшими шляхами
    """
    if start not in graph.edges:
        raise ValueError("Start node not in graph.")
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node is not None:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        current_weight = shortest_paths[current_node][1]

        for next_node, weight in destinations:
            weight += current_weight
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {
            node: shortest_paths[node] for node in shortest_paths if node not in visited
        }
        if not next_destinations:
            current_node = None
        else:
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    return {node: weight for node, (prev, weight) in shortest_paths.items()}


def visualize_graph(graph, shortest_paths, start_node):
    """
    Візуалізація графа з найкоротшими шляхами.

    :param graph: об'єкт графа
    :param shortest_paths: найкоротші шляхи від стартової вершини
    :param start_node: стартова вершина
    """
    G = nx.Graph()
    for from_node, edges in graph.edges.items():
        for to_node, weight in edges:
            G.add_edge(from_node, to_node, weight=weight)

    pos = nx.spring_layout(G)
    plt.figure()
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="skyblue",
        node_size=3000,
        font_size=18,
        font_weight="bold",
    )
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=14)

    for node, distance in shortest_paths.items():
        if node != start_node:
            path = nx.shortest_path(G, source=start_node, target=node, weight="weight")
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="r", width=2)

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plt.close()
    return img
