import matplotlib.pyplot as plt
import numpy as np
import io


def draw_branch(ax, x, y, branch_length, angle, level):
    """
    Малює одну гілку дерева Піфагора.

    :param ax: об'єкт axes для малювання
    :param x: координата x початку гілки
    :param y: координата y початку гілки
    :param branch_length: довжина гілки
    :param angle: кут розгалуження
    :param level: рівень рекурсії
    """
    if level == 0:
        return

    # Визначаємо нові координати для кінця гілки
    x_end = x + branch_length * np.cos(np.radians(angle))
    y_end = y + branch_length * np.sin(np.radians(angle))

    # Якщо рівень рекурсії 1, встановлюємо зелений колір для листя
    color = "green" if level == 1 else "brown"

    # Малюємо гілку
    ax.plot([x, x_end], [y, y_end], color=color, lw=2)

    # Малюємо праву гілку
    draw_branch(ax, x_end, y_end, branch_length * 0.7, angle - 30, level - 1)

    # Малюємо ліву гілку
    draw_branch(ax, x_end, y_end, branch_length * 0.7, angle + 30, level - 1)


def draw_tree(level):
    """
    Малює дерево Піфагора з заданим рівнем рекурсії.

    :param level: рівень рекурсії
    """
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.axis("off")

    # Початкові координати
    x = 0
    y = 0

    # Малюємо дерево Піфагора
    draw_branch(ax, x, y, 100, 90, level)

    # Зберігаємо зображення в буфер
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plt.close()
    return img
