from linked_list import create_node, append, print_list, reverse, insertion_sort, merge_sorted_lists, visualize_linked_list
from dijkstra_gui import generate_connected_random_graph, Graph, dijkstra
from dijkstra_visualization import visualize_graph
from heap_visualization import array_to_heap, draw_heap_tree, is_valid_heap
from tree_traversal_visualization import visualize_dfs, visualize_bfs
from food_selection import greedy_algorithm, dynamic_programming
from monte_carlo_dice import run_monte_carlo_simulation
from pythagoras_tree import draw_tree
import io
import matplotlib.pyplot as plt
import base64

def task_1():
    """
    Виконує завдання 1: робота з однозв'язним списком.
    """
    head = None
    head = append(head, 3)
    head = append(head, 1)
    head = append(head, 4)
    head = append(head, 2)

    output = io.StringIO()
    print("Original list:", file=output)
    print(print_list(head), file=output)
    
    head = reverse(head)
    print("\nReversed list:", file=output)
    print(print_list(head), file=output)
    
    head = insertion_sort(head)
    print("\nSorted list:", file=output)
    print(print_list(head), file=output)
    
    list1 = None
    list1 = append(list1, 1)
    list1 = append(list1, 3)
    list1 = append(list1, 5)
    
    list2 = None
    list2 = append(list2, 2)
    list2 = append(list2, 4)
    list2 = append(list2, 6)
    
    print("\nFirst sorted list:", file=output)
    print(print_list(list1), file=output)
    print("Second sorted list:", file=output)
    print(print_list(list2), file=output)
    
    merged_head = merge_sorted_lists(list1, list2)
    print("Merged sorted list:", file=output)
    print(print_list(merged_head), file=output)

    img = visualize_linked_list(merged_head)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return output.getvalue() + f'<img src="data:image/png;base64,{plot_url}" />'

def task_2(level):
    """
    Виконує завдання 2: малювання фрактала "дерево Піфагора".
    """
    img = draw_tree(level)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return f'<img src="data:image/png;base64,{plot_url}" />'

def task_3(num_nodes, num_edges, start_node):
    """
    Виконує завдання 3: алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі.
    """
    graph = generate_connected_random_graph(num_nodes, num_edges)
    shortest_paths = dijkstra(graph, start_node)

    output = io.StringIO()
    print("Shortest paths from node {}: ".format(start_node), file=output)
    for node, distance in shortest_paths.items():
        print("Distance to {}: {:.2f}".format(node, distance), file=output)

    img = visualize_graph(graph, shortest_paths, start_node)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return output.getvalue() + f'<img src="data:image/png;base64,{plot_url}" />'

def task_4(heap_array):
    """
    Виконує завдання 4: візуалізація бінарної купи.
    """
    heap_root = array_to_heap(heap_array)
    if not is_valid_heap(heap_root):
        return "Невірна структура купи"
    img = draw_heap_tree(heap_root)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return f'<img src="data:image/png;base64,{plot_url}" />'

def task_5(heap_array, traversal_method):
    """
    Виконує завдання 5: візуалізація обходу бінарного дерева.
    """
    heap_root = array_to_heap(heap_array)

    if traversal_method == 'DFS':
        img = visualize_dfs(heap_root)
    elif traversal_method == 'BFS':
        img = visualize_bfs(heap_root)
    else:
        return "Invalid traversal method."

    plot_url = base64.b64encode(img.getvalue()).decode()
    return f'<img src="data:image/png;base64,{plot_url}" />'

def task_6(budget):
    """
    Виконує завдання 6: жадібний алгоритм та динамічне програмування для вибору їжі.
    """
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    
    output = io.StringIO()
    print("Greedy Algorithm Result:", file=output)
    greedy_result = greedy_algorithm(items, budget)
    print("Selected items:", greedy_result[0], file=output)
    print("Total calories:", greedy_result[1], file=output)
    print("Total cost:", greedy_result[2], file=output)
    
    print("\nDynamic Programming Result:", file=output)
    dp_result = dynamic_programming(items, budget)
    print("Selected items:", dp_result[0], file=output)
    print("Total calories:", dp_result[1], file=output)
    print("Total cost:", dp_result[2], file=output)

    return output.getvalue()

def task_7():
    """
    Виконує завдання 7: метод Монте-Карло для визначення ймовірностей сум при киданні двох кубиків.
    """
    output = io.StringIO()
    print("Monte Carlo Dice Simulation:", file=output)
    result = run_monte_carlo_simulation(output)
    return output.getvalue() + result
