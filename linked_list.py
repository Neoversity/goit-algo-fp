import matplotlib.pyplot as plt
import io
import base64


class Node:
    """
    Клас, що представляє вузол однозв'язного списку.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


def create_node(data):
    """
    Створює новий вузол з даними.

    :param data: дані для вузла
    :return: новий вузол
    """
    return Node(data)


def append(head, data):
    """
    Додає новий вузол до кінця списку.

    :param head: голова списку
    :param data: дані для нового вузла
    :return: оновлена голова списку
    """
    new_node = create_node(data)
    if not head:
        return new_node
    last = head
    while last.next:
        last = last.next
    last.next = new_node
    return head


def print_list(head, output=None):
    """
    Друкує однозв'язний список.

    :param head: голова списку
    :param output: об'єкт для виводу (за замовчуванням - StringIO)
    :return: рядок з представленням списку
    """
    if output is None:
        output = io.StringIO()
    current = head
    while current:
        output.write(str(current.data) + " -> ")
        current = current.next
    output.write("None\n")
    return output.getvalue()


def reverse(head):
    """
    Реверсує однозв'язний список.

    :param head: голова списку
    :return: нова голова реверсованого списку
    """
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def insertion_sort(head):
    """
    Сортує однозв'язний список методом вставки.

    :param head: голова списку
    :return: нова голова відсортованого списку
    """
    sorted_head = None
    current = head
    while current:
        next_node = current.next
        sorted_head = sorted_insert(sorted_head, current)
        current = next_node
    return sorted_head


def sorted_insert(sorted_head, new_node):
    """
    Вставляє новий вузол у відсортований список.

    :param sorted_head: голова відсортованого списку
    :param new_node: новий вузол
    :return: оновлена голова відсортованого списку
    """
    if not sorted_head or sorted_head.data >= new_node.data:
        new_node.next = sorted_head
        return new_node
    current = sorted_head
    while current.next and current.next.data < new_node.data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return sorted_head


def merge_sorted_lists(head1, head2):
    """
    Об'єднує два відсортованих однозв'язних списки в один відсортований список.

    :param head1: голова першого списку
    :param head2: голова другого списку
    :return: голова об'єднаного відсортованого списку
    """
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.data < head2.data:
        head1.next = merge_sorted_lists(head1.next, head2)
        return head1
    else:
        head2.next = merge_sorted_lists(head1, head2.next)
        return head2


def visualize_linked_list(head):
    """
    Візуалізує однозв'язний список за допомогою matplotlib.

    :param head: голова списку
    :return: об'єкт зображення у форматі BytesIO
    """
    fig, ax = plt.subplots()
    ax.axis("off")
    nodes = []
    current = head
    while current:
        nodes.append(current.data)
        current = current.next
    y = [0] * len(nodes)
    ax.plot(nodes, y, "o-", ms=20, lw=2, color="skyblue")
    for i, txt in enumerate(nodes):
        ax.annotate(
            txt,
            (nodes[i], y[i]),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plt.close()
    return img


# Example usage (for testing purposes, you can remove it in the final version)
if __name__ == "__main__":
    head = None
    head = append(head, 3)
    head = append(head, 1)
    head = append(head, 4)
    head = append(head, 2)
    print(print_list(head))

    head = reverse(head)
    print(print_list(head))

    head = insertion_sort(head)
    print(print_list(head))

    head1 = None
    head1 = append(head1, 1)
    head1 = append(head1, 3)
    head1 = append(head1, 5)

    head2 = None
    head2 = append(head2, 2)
    head2 = append(head2, 4)
    head2 = append(head2, 6)

    merged_head = merge_sorted_lists(head1, head2)
    print(print_list(merged_head))

    img = visualize_linked_list(merged_head)
    with open("linked_list.png", "wb") as f:
        f.write(img.getvalue())
