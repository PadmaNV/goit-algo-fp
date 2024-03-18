import heapq
import networkx as nx
import matplotlib.pyplot as plt

"""Завдання 3. Дерева, алгоритм Дейкстри

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у
зваженому графі, використовуючи бінарну купу. Завдання включає
створення графа, використання піраміди для оптимізації вибору 
вершин та обчислення найкоротших шляхів від початкової вершини
до всіх інших."""

#Реалізація алгоритму Дейкстри з використанням бінарної купи:
def dijkstra(graph, start):
    # Ініціалізуємо словник для зберігання відстаней до кожної вершини
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Ініціалізуємо бінарну купу для вибору вершин з найменшою вагою
    priority_queue = [(0, start)]

    while priority_queue:
        # Вибираємо вершину з найменшою вагою
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо вага вершини більша, ніж відстань від стартової вершини, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Переглядаємо всіх сусідів поточної вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусіда, оновлюємо його відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def visualize_graph(graph):
    G = nx.Graph()

    # Додаємо ребра та їх ваги до графа
    for vertex, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(vertex, neighbor, weight=weight)

    # Встановлюємо позиції вершин графа
    pos = nx.spring_layout(G)

    # Рисуємо вершини графа
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue')

    # Рисуємо ребра графа та їх ваги
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Graph Visualization")
    plt.show()

# Створення графа, використовуючи піраміду для оптимізації вибору вершин:

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

print("Shortest paths from vertex", start_vertex)
for vertex, distance in shortest_paths.items():
    print("Vertex:", vertex, ", Distance:", distance)

visualize_graph(graph)

