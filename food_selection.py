def greedy_algorithm(items, budget):
    # Створення списку з елементів у вигляді (назва, вартість, калорійність, співвідношення калорій до вартості)
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']
    
    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    
    # Створення таблиці dp, де dp[i][w] - максимальна калорійність з перших i елементів з бюджетом w
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item_name, item_info = item_list[i - 1]
        cost = item_info['cost']
        calories = item_info['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Визначення вибраних елементів
    selected_items = []
    total_calories = dp[n][budget]
    w = budget
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name, item_info = item_list[i - 1]
            selected_items.append(item_name)
            w -= item_info['cost']
    
    selected_items.reverse()
    total_cost = sum(items[item]['cost'] for item in selected_items)
    
    return selected_items, total_calories, total_cost
