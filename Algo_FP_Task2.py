import turtle

"""Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” 
за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію
для створення фрактала “дерево Піфагора”. Програма має візуалізувати
фрактал “дерево Піфагора”, і користувач повинен мати можливість
вказати рівень рекурсії."""

def draw_tree(branch_length, level):
    if level == 0:
        return
    turtle.forward(branch_length)
    turtle.left(45)
    draw_tree(0.6 * branch_length, level - 1)
    turtle.right(90)
    draw_tree(0.6 * branch_length, level - 1)
    turtle.left(45)
    turtle.backward(branch_length)

def main():
    turtle.speed(9)
    turtle.left(90)
    turtle.up()
    turtle.backward(300)
    turtle.down()
    level = int(input("Введіть рівень рекурсії для фрактала: "))
    draw_tree(250, level)
    turtle.done()

if __name__ == "__main__":
    main()
