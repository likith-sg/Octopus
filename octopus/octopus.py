import hashlib

class OctopusNode:
    def __init__(self, data=None):
        self.data = data
        self.children = [None] * 8
        self.hash = None

class Octopus:
    def __init__(self, max_levels=3):
        self.root = OctopusNode()
        self.max_levels = max_levels
        self.total_nodes = 8 ** max_levels

    def _hash(self, value):
        return hashlib.sha256(value.encode()).hexdigest()

    def _get_node(self, path):
        current_node = self.root
        for index in path:
            if index < 0 or index >= 8:
                raise IndexError(f"Index {index} is out of bounds. Valid indices are from 0 to 7.")
            if not current_node.children[index]:
                raise ValueError(f"No data found at the given path: {path}.")
            current_node = current_node.children[index]
        return current_node

    def insert(self, path, data):
        if len(path) > self.max_levels:
            raise ValueError(f"Path exceeds maximum levels in the Octopus ({self.max_levels} levels).")
        current_node = self.root
        for index in path:
            if index < 0 or index >= 8:
                raise IndexError(f"Index {index} is out of bounds. Valid indices are from 0 to 7.")
            if not current_node.children[index]:
                current_node.children[index] = OctopusNode()
            current_node = current_node.children[index]
        current_node.data = data
        self.update_hashes()

    def delete(self, path):
        if len(path) > self.max_levels:
            raise ValueError(f"Path exceeds maximum levels in the Octopus ({self.max_levels} levels).")
        node = self._get_node(path)
        if node:
            node.data = None
            self.update_hashes()
        else:
            raise ValueError(f"No node found at the given path: {path}.")

    def lookup(self, path):
        if len(path) > self.max_levels:
            raise ValueError(f"Path exceeds maximum levels in the Octopus ({self.max_levels} levels).")
        node = self._get_node(path)
        return node.data if node else None

    def pathfinding(self, root_hash):
        def dfs(node, current_path):
            if not node:
                return None
            if node.hash == root_hash:
                return current_path
            for i, child in enumerate(node.children):
                result = dfs(child, current_path + [i])
                if result:
                    return result
            return None
        return dfs(self.root, [])

    def size(self):
        return self.total_nodes

    def update_hashes(self):
        def dfs(node):
            if not node:
                return ""
            if all(child is None for child in node.children):
                node.hash = self._hash(str(node.data) if node.data else "")
                return node.hash
            child_hashes = "".join(dfs(child) for child in node.children)
            node.hash = self._hash(child_hashes)
            return node.hash
        dfs(self.root)

    def solve_problem(self, func, *args, **kwargs):
        def divide_and_conquer(node):
            if not node:
                return None
            if all(child is None for child in node.children):
                return func(node, *args, **kwargs)
            results = [divide_and_conquer(child) for child in node.children if child]
            return func(node, results, *args, **kwargs)
        return divide_and_conquer(self.root)
  
