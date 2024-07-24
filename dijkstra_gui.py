import tkinter as tk
from tkinter import messagebox
import heapq
import random

class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

def dijkstra(graph, start):
    """
    Реалізація алгоритму Дейкстри для знаходження найкоротших шляхів у зваженому графі.
    
    :param graph: об'єкт графа
    :param start: початкова вершина
    :return: відстані до всіх вершин від початкової вершини
    """
    if start not in graph.edges:
        raise KeyError(f"Start node {start} not in graph")

    shortest_paths = {vertex: float('infinity') for vertex in graph.edges}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > shortest_paths[current_vertex]:
            continue

        for neighbor in graph.edges[current_vertex]:
            weight = graph.weights.get((current_vertex, neighbor), float('infinity'))
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths

def generate_connected_random_graph(num_nodes, num_edges):
    graph = Graph()
    nodes = [str(i) for i in range(1, num_nodes + 1)]
    
    # Create a connected graph (tree) first
    for i in range(1, num_nodes):
        from_node = nodes[i - 1]
        to_node = nodes[i]
        weight = random.uniform(1, 100)
        graph.add_edge(from_node, to_node, weight)
    
    # Add additional edges to meet the num_edges requirement
    additional_edges = num_edges - (num_nodes - 1)
    while additional_edges > 0:
        from_node = random.choice(nodes)
        to_node = random.choice(nodes)
        if from_node != to_node and (from_node, to_node) not in graph.weights and (to_node, from_node) not in graph.weights:
            weight = random.uniform(1, 100)
            graph.add_edge(from_node, to_node, weight)
            additional_edges -= 1
    
    return graph
