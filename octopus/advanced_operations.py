from .octopus import Octopus

class AdvancedOperations:
    def __init__(self, octopus):
        if not isinstance(octopus, Octopus):
            raise TypeError("Expected an Octopus instance.")
        self.octopus = octopus

    def batch_insert(self, paths, data):
        if len(paths) != len(data):
            raise ValueError("Paths and data must have the same length.")
        for path, datum in zip(paths, data):
            self.octopus.insert(path, datum)

    def batch_delete(self, paths):
        if not paths:
            raise ValueError("Paths cannot be empty.")
        for path in paths:
            self.octopus.delete(path)

    def subtree_extraction(self, path):
        if len(path) > self.octopus.max_levels:
            raise ValueError(f"Path exceeds maximum levels in the Octopus ({self.octopus.max_levels} levels).")
        node = self.octopus._get_node(path)
        if node:
            return node
        raise ValueError(f"No subtree found at the given path: {path}.")

    def hash_validation(self):
        def dfs(node):
            if not node:
                return ""
            if all(child is None for child in node.children):
                return self.octopus._hash(str(node.data) if node.data else "")
            child_hashes = "".join(dfs(child) for child in node.children)
            return self.octopus._hash(child_hashes)
        return dfs(self.octopus.root) == self.octopus.root.hash

    def divide_and_conquer(self, func, *args, **kwargs):
        if not callable(func):
            raise TypeError("The provided function is not callable.")
        return self.octopus.solve_problem(func, *args, **kwargs)
  
