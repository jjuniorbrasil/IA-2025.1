import os
import random

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent: Node = parent
        self.left: Node = None
        self.right: Node = None

    def path(self):
        node = self
        path_nodes = []

        while node:
            path_nodes.append(node)
            node = node.parent

        path_nodes.reverse()
        return [n.state for n in path_nodes]

class Tree:
    def __init__(self, state):
        self.root = Node(state)
        self.goal = ''
        print("Arvore criada. Raiz: ", self.root.state, "\n")

    def addNode(self, state):
        current = self.root
        while current:
            if state == current.state:
                return

            if state > current.state:
                if current.right is None:
                    current.right = Node(state, current)
                    print("Nó ", state, " adicionado à direita de ", current.state, ".")
                    return
                current = current.right
            else:
                if current.left is None:
                    current.left = Node(state, current)
                    print("Nó ", state, " adicionado à esquerda de ", current.state, ".")
                    return
                current = current.left

def newTreeExample(root = 50, nodeNumber = 20):
    os.system('cls' if os.name == 'nt' else 'clear')
    tree = Tree(50)

    for _ in range(nodeNumber):
        num = random.randint(0, 100)
        tree.addNode(num)

    return tree