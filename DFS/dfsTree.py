'''
    função BUSCA-EM-PROFUNDIDADE-LIMITADA (problema, limite) retorna uma solução ou falha/corte
    retornar BPL-RECURSIVA(CRIAR-NÓ(problema, ESTADO-INICIAL), problema, limite)

    função BPL-RECURSIVA(nó, problema, limite) retorna uma solução ou falha/corte
        
        se problema.TESTAR-OBJETIVO(nó.ESTADO) então retorna SOLUÇÃO(nó)
        se não se limite = 0 então retorna corte
        senão
            corte_ocorreu? <- falso para cada ação no problema.AÇÕOES(nó.ESTADO) faça
                filho <- NÓ-FILHO (problema, nó, ação)
                resultado <- BPL-RECURSIVA(criança, problema, limite - 1)

                se resultado = corte então corte_ocorreu <- verdadeiro
                senão se resultado = falha então retorna resultado
                se corte_ocorreu? então retorna corte senão retorna falha
'''

from components.tree import Node, Tree, newTreeExample

def solution(node: Node):
    return node.path()

def depthFirstSearch(problem: Tree, goal):
    return depthFirstSearchRecursive(problem.root, goal)

def depthFirstSearchRecursive(node: Node, goal):
    if node.state == goal:
        return solution(node)

    else:
        if node.left:
            result = depthFirstSearchRecursive(node.left, goal)
            if result:
                return result

        if node.right:
            result = depthFirstSearchRecursive(node.right, goal)
            if result:
                return result

        return None

def simulation(searchFor=20):
  result = None

  while not result:
    result = depthFirstSearch(newTreeExample(root=50, nodeNumber=10), searchFor)

  print(f"\nBuscando por: {searchFor}")
  print(f"Caminho: {result}")

simulation(25)