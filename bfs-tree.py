
---

### ✅ Python Code (`bfs_tree.py`)

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

def bfs(tree, node, key_node=None, queue=[]):
    if node == key_node:
        return route_finder(tree, node, [node])
    else:
        if not len(queue):
            queue.append(node)
        print(queue)
        if node in tree:
            for child in tree[node]:
                queue.append(child)
        queue.pop(0)
        return bfs(tree, queue[0], key_node, queue)

def route_finder(tree, node, route_list):
    for parent, child in tree.items():
        if node in child:
            route_list.insert(0, parent)
            break
    if route_list[0] != list(tree.keys())[0]:
        route_finder(tree, route_list[0], route_list)
    return route_list

# Run the search
goal = "G"
print(f"goal node is {goal}\nSearching...")
route = bfs(tree, list(tree.keys())[0], goal)
print("The route is " + " -> ".join(str(item) for item in route))
