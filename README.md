# Breadth-First Search (BFS) Tree Traversal in Python

This project implements a basic **Breadth-First Search (BFS)** algorithm to traverse a predefined tree structure and find a goal node. Once the goal is found, it backtracks the path from the root to the goal using a route-finder function.

---

## 🌳 Tree Structure

The tree is represented using a Python dictionary:

```python
tree = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I'],
    'E': ['J'],
    'F': [],
    'G': ['K'],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}

🔍 Goal
Given a goal node (e.g., "G"), the script performs BFS to locate it and then finds the route from the root to that node.

🧠 Functions Explained
1. bfs(tree, node, key_node, queue=[])
Performs BFS recursively.

Keeps track of visited nodes using the queue.

Stops when the goal node is found and calls route_finder().

2. route_finder(tree, node, route_list)
Backtracks from the goal node to the root node using parent-child relationships in the tree.
🧪 Example Output
css
Copy
Edit
goal node is G
Searching...
['A']
['B', 'C', 'D']
['C', 'D', 'E', 'F']
['D', 'E', 'F', 'G', 'H']
['E', 'F', 'G', 'H', 'I']
['F', 'G', 'H', 'I', 'J']
The route is A -> C -> G
🏃 How to Run
Clone the repo:

bash
Copy
Edit
git clone https://github.com/your-username/bfs-tree-python.git
cd bfs-tree-python
Run the Python script:

bash
Copy
Edit
python bfs_tree.py
