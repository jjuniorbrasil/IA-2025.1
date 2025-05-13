'''
função BUSCA-EM-LARGURA(problema)
  retorna uma solução ou falha

  nó ← um nó com ESTADO = problema.ESTADO-INICIAL, CUSTO-DE-CAMINHO = 0
  
  se problema.TESTE-DE-OBJETIVO(nó.ESTADO) então
    retorne SOLUÇÃO(nó)

  borda ← uma fila FIFO com nó como elemento único
  explorado ← conjunto vazio

  repita
    se VAZIO?(borda) então
      retorne falha

    nó ← POP(borda)  /* escolhe o nó mais raso na borda */
    adicione nó.ESTADO para explorado

    para cada ação em problema.AÇÕES(nó.ESTADO) faça
      filho ← NÓ-FILHO(problema, nó, ação)
      
      se (filho.ESTADO) não está em explorado ou borda então
        se problema.TESTE-DE-OBJETIVO(filho.ESTADO) então
          retorne SOLUÇÃO(filho)
        
        borda ← INSIRA(filho, borda)
'''

from components.brFSProblem import Node, Problem, bcolors, solution, actions

def brFS(problem: Problem):
    node: Node = Node(problem.initialState)

    if problem.goalTest(node.state): 
            return solution(node)

    border: list[Node] = [node]
    explored = set()

    while border:
        node = border.pop(0)
        print(bcolors.OKBLUE + f"{node.state} escolhido para ser expandido." + bcolors.ENDC)

        explored.add(node.state)

        for [actionState] in problem.action(node.state):
            childNode = Node(state = actionState, parent = node)

            if childNode.state not in explored and childNode.state not in [n.state for n in border]:
                if problem.goalTest(node.state):
                  print('Estado encontrado:', node.state) 
                  return solution(node)
                print(bcolors.OKGREEN + f"\t(Adicionando {childNode.state} à borda)" + bcolors.ENDC)
                border.append(childNode)
                
problem = Problem('A', 'G', actions)

brFS(problem)