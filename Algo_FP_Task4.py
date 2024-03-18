import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, traversal_order=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(traversal_order)
    plt.show()

def build_heap_tree(heap):
    n = len(heap)

    def heapify(heap, n, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and heap[left] is not None and heap[left] > heap[largest]:
            largest = left

        if right < n and heap[right] is not None and heap[right] > heap[largest]:
            largest = right

        if largest != index:
            heap[index], heap[largest] = heap[largest], heap[index]
            heapify(heap, n, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(heap, n, i)

    root = Node(heap[0])
    queue = [root]
    i = 0

    while queue:
        node = queue.pop(0)
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < n and heap[left_index] is not None:
            node.left = Node(heap[left_index])
            queue.append(node.left)

        if right_index < n and heap[right_index] is not None:
            node.right = Node(heap[right_index])
            queue.append(node.right)

        i += 1

    return root

# heap_array = [0, 4, 5, 10, 1, 3]  
heap_array = [2, 3, 5, 8, 11, 9, 4, 44, 2, 72,59, 88]
root = build_heap_tree(heap_array)


if __name__ == "__main__":
    draw_tree(root)
