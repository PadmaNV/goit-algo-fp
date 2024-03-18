import random

def roll_dice():
    return random.randint(1, 6)

def monte_carlo_simulation(num_trials):
    results = {i: 0 for i in range(2, 13)}  # Словник для збереження кількості випадань кожної суми
    
    for _ in range(num_trials):
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2
        results[total] += 1
    
    probabilities = {k: f"{v / num_trials * 100:.2f}% ({round(v/num_trials*36)}/{36})" for k, v in results.items()}  # Обчислення ймовірностей у відсотках
    
    return probabilities

def print_probabilities(probabilities):
    print("Сума\tІмовірність")
    for total, probability in probabilities.items():
        print(f"{total}\t{probability}")

def main():
    num_trials = 1000000
    probabilities = monte_carlo_simulation(num_trials)
    print_probabilities(probabilities)

if __name__ == "__main__":
    main()
