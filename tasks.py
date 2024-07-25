from linked_list import (
    create_node,
    append,
    print_list,
    reverse,
    insertion_sort,
    merge_sorted_lists,
    visualize_linked_list,
)
from dijkstra_visualization import (
    generate_connected_random_graph,
    Graph,
    dijkstra,
    visualize_graph,
)
from heap_visualization import array_to_heap, draw_heap_tree, is_valid_heap
from tree_traversal_visualization import visualize_dfs, visualize_bfs
from food_selection import greedy_algorithm, dynamic_programming
from monte_carlo_dice import run_monte_carlo_simulation
from pythagoras_tree import draw_tree
import io
import base64


def task_1():
    """
    Завдання 1: Операції з однозв'язним списком.
    Створення списку, реверсування, сортування та об'єднання списків.
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
    Завдання 2: Малювання фрактала дерева Піфагора.

    :param level: рівень рекурсії
    :return: HTML-код зображення фрактала
    """
    img = draw_tree(level)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return f'<img src="data:image/png;base64,{plot_url}" />'


def task_3(num_nodes, num_edges, start_node):
    """
    Завдання 3: Алгоритм Дейкстри для знаходження найкоротших шляхів у графі.

    :param num_nodes: кількість вузлів
    :param num_edges: кількість ребер
    :param start_node: початковий вузол
    :return: HTML-код результатів та зображення графа
    """
    if num_nodes < 2:
        return "Number of nodes must be at least 2."
    if num_edges < num_nodes - 1:
        return "Number of edges must be at least number of nodes minus one for a connected graph."
    if num_edges > num_nodes * (num_nodes - 1) / 2:
        return "Too many edges for the given number of nodes."

    try:
        graph = generate_connected_random_graph(num_nodes, num_edges)
        shortest_paths = dijkstra(graph, start_node)

        output = io.StringIO()
        print("Shortest paths from node {}: ".format(start_node), file=output)
        for node, distance in shortest_paths.items():
            print("Distance to {}: {:.2f}".format(node, distance), file=output)

        img = visualize_graph(graph, shortest_paths, start_node)
        plot_url = base64.b64encode(img.getvalue()).decode()

        return output.getvalue() + f'<img src="data:image/png;base64,{plot_url}" />'
    except ValueError as e:
        return str(e)


def task_4(heap_array):
    """
    Завдання 4: Візуалізація бінарної купи.

    :param heap_array: масив для побудови купи
    :return: HTML-код зображення купи
    """
    heap_root = array_to_heap(heap_array)
    if not is_valid_heap(heap_root):
        return "Невірна структура купи"
    img = draw_heap_tree(heap_root)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return f'<img src="data:image/png;base64,{plot_url}" />'


def task_5(heap_array, traversal_method):
    """
    Завдання 5: Візуалізація обходу дерева.

    :param heap_array: масив для побудови дерева
    :param traversal_method: метод обходу (DFS або BFS)
    :return: HTML-код зображення дерева
    """
    heap_root = array_to_heap(heap_array)

    if traversal_method == "DFS":
        img = visualize_dfs(heap_root)
    elif traversal_method == "BFS":
        img = visualize_bfs(heap_root)
    else:
        return "Invalid traversal method."

    plot_url = base64.b64encode(img.getvalue()).decode()
    return f'<img src="data:image/png;base64,{plot_url}" />'


def task_6(budget):
    """
    Завдання 6: Вибір їжі з найбільшою сумарною калорійністю в межах бюджету.

    :param budget: заданий бюджет
    :return: HTML-код результатів
    """
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
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
    Завдання 7: Імітація методом Монте-Карло для визначення ймовірностей сум при киданні двох кубиків.

    :return: HTML-код результатів та графіка
    """
    output = io.StringIO()
    print("Monte Carlo Dice Simulation:", file=output)
    result = run_monte_carlo_simulation(output)
    return output.getvalue() + result
