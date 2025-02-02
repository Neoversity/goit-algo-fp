import random
import matplotlib.pyplot as plt
import io
import base64

def monte_carlo_simulation(num_rolls):
    """
    Імітує кидки двох кубиків і підраховує кількість появ кожної можливої суми.

    :param num_rolls: Кількість імітованих кидків
    :return: Словник ймовірностей для кожної суми та кількість появ кожної суми
    """
    # Ініціалізація словника для підрахунку кількості появ кожної суми
    sum_counts = {i: 0 for i in range(2, 13)}

    # Імітація кидків кубиків
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll_sum = roll1 + roll2
        sum_counts[roll_sum] += 1

    # Обчислення ймовірностей
    probabilities = {k: v / num_rolls for k, v in sum_counts.items()}

    return probabilities, sum_counts

def plot_probabilities(probabilities):
    """
    Створює графік ймовірностей для кожної суми при киданні двох кубиків.

    :param probabilities: Словник ймовірностей для кожної суми
    """
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, color="skyblue")
    plt.xlabel("Сума")
    plt.ylabel("Імовірність")
    plt.title("Ймовірності сум при киданні двох кубиків (метод Монте-Карло)")
    plt.xticks(sums)
    plt.grid(axis="y")

def run_monte_carlo_simulation(output):
    """
    Запускає симуляцію методом Монте-Карло, виводить результати у консоль і повертає графік у вигляді HTML-коду.

    :param output: Об'єкт для виводу результатів (наприклад, sys.stdout або файл)
    :return: HTML-код графіка
    """
    num_rolls = 1000000  # Кількість імітованих кидків
    probabilities, sum_counts = monte_carlo_simulation(num_rolls)

    # Виведення ймовірностей у консоль
    print("Ймовірності сум при киданні двох кубиків (метод Монте-Карло):", file=output)
    for sum_, prob in probabilities.items():
        print(
            f"Сума: {sum_}, Імовірність: {prob:.2%} ({sum_counts[sum_]} разів)",
            file=output,
        )

    # Побудова графіка ймовірностей
    plot_probabilities(probabilities)
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return f'<img src="data:image/png;base64,{plot_url}" />'
