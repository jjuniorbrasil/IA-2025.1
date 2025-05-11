'''

função BUSCA-DE-CUSTO-UNIFORME(problema)
  retorna uma solução ou falha

  nó ← um nó com ESTADO = problema.ESTADO-INICIAL, CUSTO-DE-CAMINHO = 0

  borda ← uma fila FIFO com nó como elemento único
  explorado ← conjunto vazio

  repita
    se VAZIO?(borda) então
      retorne falha

    nó ← POP(borda)  /* escolhe o nó mais raso na borda */
    se problema.TESTE-DE-OBJETIVO(nó.ESTADO) então
    retorne SOLUÇÃO(nó)
    adicione nó.ESTADO para explorado

    para cada ação em problema.AÇÕES(nó.ESTADO) faça
      filho ← NÓ-FILHO(problema, nó, ação)
      
      se (filho.ESTADO) não está em explorado ou borda então
			  borda ← INSIRA(filho, borda)
			senao se (filho.ESTADO) está na borda com o maior CUSTO-DE-CAMINHO então
				substituir aquele nó borda por filho

'''

from components.ucsProblem import Node, Problem, bcolors, solution, actionsNE, actions

def uCS(problem: Problem):
    node: Node = Node(problem.initialState)
    border: list[Node] = [node]
    explored = set()

    while border:
        node = border.pop(0)
        print(bcolors.OKBLUE + f"{node.state} escolhido para ser expandido. (custo a partir da origem: {node.cost})" + bcolors.ENDC)

        if problem.goalTest(node.state): 
            return solution(node)
        explored.add(node.state)

        for [actionState, actionCost] in problem.action(node.state):
            childNode = Node(state = actionState, cost = node.cost + actionCost, parent = node)

            if (childNode.state != problem.initialState):
                print(f"\tExaminando: {node.state} a {childNode.state} - custo a partir da origem: {childNode.cost}")

            if childNode.state not in explored and childNode.state not in [n.state for n in border]:
                print(bcolors.OKGREEN + f"\t(Adicionando {childNode.state} à borda)" + bcolors.ENDC)
                border.append(childNode)
            else:
                for i, existing in enumerate(border):
                    if existing.state == childNode.state and existing.cost > childNode.cost:
                        border[i] = childNode
                        break
        
        border.sort(key=lambda x: x.cost)
        print(bcolors.WARNING + '\nReordenando borda e escolhendo novo nó com menor custo a ser expandido.\n' + bcolors.ENDC)

    return print(bcolors.FAIL + "Falha: objetivo não encontrado." + bcolors.ENDC)

# problem = Problem('São Luís', 'Campinas', actionsNE)
problem = Problem('Sibiu', 'Bucharest', actions)

uCS(problem)