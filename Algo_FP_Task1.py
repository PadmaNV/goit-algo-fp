"""Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту)
необхідно:

 -- написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи
посилання між вузлами;
 -- розробити алгоритм сортування для однозв'язного списку, наприклад, сортування
вставками або злиттям;
 -- написати функцію, що об'єднує два відсортовані однозв'язні списки в один
відсортований список."""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

#Алгоримт сортування вставками:
    def sort(self):
        if self.head is None:
            return
        sorted_head = None
        current = self.head
        while current:
            next_node = current.next
            if sorted_head is None or sorted_head.data >= current.data:
                current.next = sorted_head
                sorted_head = current
            else:
                search = sorted_head
                while search.next is not None and search.next.data < current.data:
                    search = search.next
                current.next = search.next
                search.next = current
            current = next_node
        self.head = sorted_head

    def merge_sorted_lists(self, llist):
        # Створюємо новий список для об'єднання
        merged_list = LinkedList()

        # Покажчики на початок вхідних списків
        p = self.head
        q = llist.head

        # Поки є елементи в обох списках
        while p is not None and q is not None:
            # Додаємо менший елемент з першого або другого списку в залежності від їх значень
            if p.data <= q.data:
                merged_list.append(p.data)
                p = p.next
            else:
                merged_list.append(q.data)
                q = q.next

        # Якщо в першому списку залишилися елементи, додаємо їх до об'єднаного списку
        while p is not None:
            merged_list.append(p.data)
            p = p.next

        # Якщо в другому списку залишилися елементи, додаємо їх до об'єднаного списку
        while q is not None:
            merged_list.append(q.data)
            q = q.next

        # Сортуємо об'єднаний список після об'єднання
        merged_list.sort()

        return merged_list.head
    

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


# Приклад використання

# Створення списків
list1 = LinkedList()
list1.append(3)
list1.append(1)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(6)
list2.append(4)

# Відображення початкових списків
print("Перший список:")
list1.display()
print("Другий список:")
list2.display()

# Реверсування першого списку
list1.reverse()
print("Перший список після реверсування:")
list1.display()

# Об'єднання двох відсортованих списків
merged_list = LinkedList()
merged_list.head = list1.merge_sorted_lists(list2)
print("Об'єднаний відсортований список:")
merged_list.display()
