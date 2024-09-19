def hamiltonian_circuit(graph, path):
  """
  Verifica a existência de um circuito Hamiltoniano em um grafo.

  Args:
    graph: Uma matriz de adjacência representando o grafo.
    path: Uma lista representando o caminho atual.

  Returns:
    True se um circuito Hamiltoniano for encontrado, False caso contrário.
  """

  n = len(graph)
  if len(path) == n:
    # Se o caminho tem o tamanho do grafo e o último vértice é adjacente ao primeiro,
    # então encontramos um circuito Hamiltoniano.
    return graph[path[0]][path[-1]] == 1

  for v in range(n):
    # Verifica se o vértice não está já no caminho e se há uma aresta para ele.
    if v not in path and graph[path[-1]][v] == 1:
      path.append(v)
      if hamiltonian_circuit(graph, path):
        return True
      path.pop()

  return False

# Exemplo de uso
graph = [
  [0, 1, 0, 1, 0],
  [1, 0, 1, 1, 1],
  [0, 1, 0, 0, 1],
  [1, 1, 0, 0, 1],
  [0, 1, 1, 1, 0]
]

# Iniciando o caminho com o vértice 0
path = [0]

if hamiltonian_circuit(graph, path):
  print("Um circuito Hamiltoniano existe.")
else:
  print("Não existe um circuito Hamiltoniano.")