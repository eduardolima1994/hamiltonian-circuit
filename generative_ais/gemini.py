def hamiltonian_circuit(graph, path, visited):
  """
  Função para encontrar um circuito hamiltoniano.

  Args:
    graph: Matriz de adjacência do grafo.
    path: Lista representando o caminho atual.
    visited: Conjunto dos vértices já visitados.

  Returns:
    True se um circuito hamiltoniano for encontrado, False caso contrário.
  """

  n = len(graph)
  last_vertex = path[-1]

  if len(path) == n and graph[last_vertex][path[0]] == 1:
    return True

  for vertex in range(n):
    if not visited[vertex] and graph[last_vertex][vertex] == 1:
      path.append(vertex)
      visited.add(vertex)

      if hamiltonian_circuit(graph, path, visited):
        return True

      path.pop()
      visited.remove(vertex)

  return False

def find_hamiltonian_circuit(graph):
  """
  Função principal para encontrar um circuito hamiltoniano.

  Args:
    graph: Matriz de adjacência do grafo.

  Returns:
    Uma lista representando o circuito hamiltoniano, caso exista.
    None, caso contrário.
  """

  n = len(graph)
  for start in range(n):
    path = [start]
    visited = set([start])
    if hamiltonian_circuit(graph, path, visited):
      return path
  return None

# Exemplo de uso:
graph = [
  [0, 1, 0, 1],
  [1, 0, 1, 1],
  [0, 1, 0, 1],
  [1, 1, 1, 0]
]

result = find_hamiltonian_circuit(graph)
if result:
  print("Circuito Hamiltoniano encontrado:", result)
else:
  print("Nenhum circuito Hamiltoniano encontrado.")