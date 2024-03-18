"""Завдання 6:

Програмно реалізовано функцію, яка використовує принцип
жадібного алгоритму. Код виконується і повертає назви страв, 
максимізуючи співвідношення калорій до вартості, не 
перевищуючи заданий бюджет.

Програмно реалізовано функцію, яка використовує принцип 
динамічного програмування. Код виконується і повертає 
оптимальний набір страв для максимізації калорійності 
при заданому бюджеті."""



def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            total_cost += data['cost']
            total_calories += data['calories']
            chosen_items.append(item)

    return chosen_items, total_calories

def dynamic_programming(items, budget):
    keys = list(items.keys())
    n = len(keys)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if items[keys[i - 1]]['cost'] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[keys[i - 1]]['cost']] + items[keys[i - 1]]['calories'])

    chosen_items = []
    total_calories = dp[n][budget]
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            chosen_items.append(keys[i - 1])
            j -= items[keys[i - 1]]['cost']

    return chosen_items, total_calories


# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = int(input("Введіть бюджет: "))
50
# Виклик жадібного алгоритму
greedy_items, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_items)
print("Сумарна калорійність:", greedy_calories)

# Виклик алгоритму динамічного програмування
dynamic_items, dynamic_calories = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Вибрані страви:", dynamic_items)
print("Сумарна калорійність:", dynamic_calories)
