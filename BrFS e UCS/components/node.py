class Node:
    def __init__(self, state: str, cost: int = 0, parent = None):
        self.state = state
        self.cost = cost
        self.parent = parent
        
    def __repr__(self):
        return f"Node({self.state}, {self.cost})"
    
    def path(self):
        node = self
        path_nodes = []

        while node:
            path_nodes.append(node)
            node = node.parent

        path_nodes.reverse()
        return [n.state for n in path_nodes]
    