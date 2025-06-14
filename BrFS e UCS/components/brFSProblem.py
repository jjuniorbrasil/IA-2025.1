class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

actions = {
    'A': [('B'), ('C')],
    'B': [('D'), ('E')],
    'C': [('F'), ('G')],
    'D': [('H'), ('I')],
    'E': [('J'), ('K')],
    'F': [('L'), ('M')],
    'G': [('N'), ('O')],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}

from components.node import Node
class Problem:
    def __init__(self, initialState: str, goal: str, actions):
        self.initialState = initialState
        self.goal = goal
        self.actions = actions
        print(bcolors.OKCYAN + f"\nProblema criado - ESTADO INICIAL: {self.initialState}, OBJETIVO: {self.goal}\n" + bcolors.ENDC)

    def goalTest(self, state: str):
        return self.goal == state

    def action(self, state):
        return self.actions.get(state, [])
    
def solution(node: Node):
    print(f"\n\tSolução encontrada até: {bcolors.UNDERLINE + bcolors.FAIL + node.state + bcolors.ENDC}")
    print("\t" + node.path().__str__())