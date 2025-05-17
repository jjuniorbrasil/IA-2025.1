'''
    função BUSCA-EM-PROFUNDIDADE-LIMITADA (problema, limite) retorna uma solução ou falha/corte
    retornar BPL-RECURSIVA(CRIAR-NÓ(problema, ESTADO-INICIAL), problema, limite)

    função BPL-RECURSIVA(nó, problema, limite) retorna uma solução ou falha/corte
        
        se problema.TESTAR-OBJETIVO(nó.ESTADO) então retorna SOLUÇÃO(nó)
        se não se limite = 0 então retorna corte
        senão
            corte_ocorreu? <- falso 
            para cada ação no problema.AÇÕES(nó.ESTADO) faça
                filho <- NÓ-FILHO (problema, nó, ação)
                resultado <- BPL-RECURSIVA(criança, problema, limite - 1)

                se resultado = corte então 
                    corte_ocorreu <- verdadeiro
                senão se resultado = falha então 
                    retorna resultado
                
                se corte_ocorreu? então 
                    retorna corte 
                senão retorna falha
'''

from components.node import Node
from components.problem import Problem, bcolors
from components.actions import dfs_actions

def solution(node: Node):
    return f"Encontrou '{node.state}': " + str(node.path())

def depthFirstSearch(problem: Problem, limit: int):
    return depthFirstSearchRecursive(Node(problem=problem, state=problem.initialState), problem, limit)

def depthFirstSearchRecursive(node: Node, problem: Problem, limit: int):
    print(bcolors.OKGREEN + f"\nNo nó: {node.state}" + bcolors.ENDC)
    if problem.goalTest(node.state):
        return solution(node)
    elif limit == 0:
        return 'cut'
    
    else:
        cut_happened = False

        for actionState in problem.action(node.state):
            print(bcolors.WARNING + f"\tDe {node.state}, verificando: {actionState}" + bcolors.ENDC)
            if actionState is None: print('Sem filhos.')
            child = Node(state=actionState, parent=node, problem=problem)
            result = depthFirstSearchRecursive(child, problem, limit - 1)

            if result == 'Corte: busca encerrada':
                cut_happened = True
            elif result != 'Falha':
                return result
            
        
        return 'cut' if cut_happened else 'failure'

problem = Problem('A', 'P', dfs_actions)
result = depthFirstSearch(problem, 4)
print("\n" + str(result))