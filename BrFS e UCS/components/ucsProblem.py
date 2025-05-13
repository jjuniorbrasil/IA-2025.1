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
    'Arad': [('Zerind', 75), ('Sibiu', 140),('Timisoara', 118)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80), ('Arad', 140)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Bucharest', 101), ('Craiova', 138)],
    'Bucharest': [('Pitesti', 101), ('Fagaras', 211), ('Giurgiu', 90)]
}

actionsNE = {
    'São Luís': [('Teresina', 446), ('Fortaleza', 1075)],
    'Teresina': [('São Luís', 446), ('Fortaleza', 636), ('Picos', 310)],
    'Fortaleza': [('Teresina', 636), ('São Luís', 1075), ('Natal', 537)],
    'Picos': [('Teresina', 310), ('Juazeiro do Norte', 362)],
    'Juazeiro do Norte': [('Picos', 362), ('Campina Grande', 509)],
    'Natal': [('Fortaleza', 537), ('João Pessoa', 185)],
    'João Pessoa': [('Natal', 185), ('Campina Grande', 120), ('Recife', 120)],
    'Campina Grande': [('Juazeiro do Norte', 509), ('João Pessoa', 120)],
    'Recife': [('João Pessoa', 120)]
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
    
def orderHandler(node: Node): 
    return node.cost

def solution(node: Node):
    print(f"\n\tSolução encontrada até: {bcolors.UNDERLINE + bcolors.FAIL + node.state + bcolors.ENDC}")
    print("\t" + node.path().__str__())
    print(f"\tDistância: {node.cost}\n")