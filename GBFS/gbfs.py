# Implementando 'Busca Gulosa de Melhor Escolha' através de alterações na busca de custo uniforme

from components.node import Node
from components.problem import Problem, bcolors
from components.actions import actions, straigth_line_distance_to_bucharest_from

def heuristicFunction(state):
    return straigth_line_distance_to_bucharest_from.get(state)


def avaliationFunction(node):
    return heuristicFunction(node.state)

def solution(node: Node):
    print(f"\n\tSolução encontrada até: {bcolors.UNDERLINE + bcolors.FAIL + node.state + bcolors.ENDC}")
    print("\t" + node.path().__str__())
    print(f"\tDistância: {node.cost}\n")

def greedyBestFirstSearch(problem: Problem):
    node: Node = Node(problem.initialState)
    border: list[Node] = [node]
    # explored = set()

    while border:
        node = border.pop(0)
        print(bcolors.OKBLUE + f"{node.state} escolhido para ser expandido. (custo a partir da origem: {node.cost})" + bcolors.ENDC)

        if problem.goalTest(node.state): 
            return solution(node)
        # explored.add(node.state) # não trackearemos mais os nós explorados

        for [actionState, actionCost] in problem.action(node.state):
            childNode = Node(state = actionState, cost = node.cost + actionCost, parent = node)

            if (childNode.state != problem.initialState):
                print(f"\tExaminando: {node.state} a {childNode.state} - custo a partir da origem: {childNode.cost}")

            if childNode.state not in [n.state for n in border]:
                print(bcolors.OKGREEN + f"\t(Adicionando {childNode.state} à borda)" + bcolors.ENDC)
                border.append(childNode)
            else:
                for i, existing in enumerate(border):
                    if existing.state == childNode.state and existing.cost > childNode.cost:
                        border[i] = childNode
                        break
        
        border.sort(key=avaliationFunction)
        print(bcolors.WARNING + '\nReordenando borda e escolhendo novo nó com menor custo ESTIMADO por h(n).\n' + bcolors.ENDC)

    return print(bcolors.FAIL + "Falha: objetivo não encontrado." + bcolors.ENDC)

problem = Problem('Arad', 'Bucharest', actions)

greedyBestFirstSearch(problem)