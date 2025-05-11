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

from util.tree import Tree, newTreeExample

def brFS(problem: Tree, goal):
    node = problem.root

    border = [node]
    explored = []
      
    while border:
      node = border.pop(0)
      explored.append(node.state)
 
      if node.state == goal:
       return [node.path(), explored.__str__()]
      
      if node.left is not None:
         border.append(node.left)
      if node.right is not None:
         border.append(node.right)

    return None

def simulation(searchFor=20):
  [path, explored] = [None, None]

  while not path and not explored:
    result = brFS(newTreeExample(root=50, nodeNumber=10), searchFor)

    if result is not None:
      [path, explored] = result 

  print(f"\nBuscando por: {searchFor}")
  print(f"Caminho encontrado: {path}")
  print(f"Explorados até o caminho: {explored}\n")

simulation()