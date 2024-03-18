from Algo_FP_Task4 import build_heap_tree, add_edges, draw_tree, Node

import uuid
import networkx as nx
import matplotlib.pyplot as plt


def depth_first_search(node, traversal_order):
    if node is not None:
        traversal_order.append(node)
        depth_first_search(node.left, traversal_order)
        depth_first_search(node.right, traversal_order)

def breadth_first_search(root, traversal_order):
    if root is None:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        traversal_order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
           
def visualize_traversal(root, traversal_function, traversal_name, start_color="#000080", brightness_increase=25):
    traversal_order = []
    traversal_function(root, traversal_order)
    
    start_r = int(start_color[1:3], 16)  # Розбираємо початковий колір на компоненти RGB
    start_g = int(start_color[3:5], 16)
    start_b = int(start_color[5:7], 16)
    
    for i, node in enumerate(traversal_order):
        # Збільшуємо значення яскравості на декілька тонів для кожного наступного кольору
        r = min(255, start_r + i * brightness_increase)
        g = min(255, start_g + i * brightness_increase)
        b = min(255, start_b + i * brightness_increase)
        
        # Генеруємо код кольору в форматі RGB
        color_code = "#{:02X}{:02X}{:02X}".format(r, g, b)
        
        # Присвоюємо кольору вузла згенерований колір
        node.color = color_code
        
        # Візуалізуємо кожний крок обходу
        draw_tree(root, traversal_name)


# heap_array = [0, 4, 5, 10, 1, 3]  
heap_array1 = [2, 3, 5, 8, 11, 9, 4, 44, 2, 72]
root1 = build_heap_tree(heap_array1)

print("Обхід DFS:")
visualize_traversal(root1, depth_first_search, "DFS", '#191970')
print("Обхід BFS:")
visualize_traversal(root1, breadth_first_search, "BFS", '#800000')