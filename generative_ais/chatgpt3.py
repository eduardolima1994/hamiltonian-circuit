def is_valid(v, pos, path, graph):
    # Verifica se o vértice v é adjacente ao último vértice do caminho
    if graph[path[pos - 1]][v] == 0:
        return False

    # Verifica se o vértice já está no caminho
    if v in path:
        return False

    return True

def hamiltonian_util(graph, path, pos):
    # Se todos os vértices estão incluídos no caminho
    if pos == len(graph):
        # E se há um arco do último vértice ao primeiro vértice
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    # Tenta diferentes vértices como próximo vértice do caminho
    for v in range(1, len(graph)):
        if is_valid(v, pos, path, graph):
            path[pos] = v

            if hamiltonian_util(graph, path, pos + 1):
                return True

            # Se adicionar v não leva a uma solução, remova v
            path[pos] = -1

    return False

def hamiltonian(graph):
    path = [-1] * len(graph)
    path[0] = 0  # Começa do primeiro vértice

    if not hamiltonian_util(graph, path, 1):
        return False
    return True

# Exemplo de uso
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

if hamiltonian(graph):
    print("O grafo possui um Circuito Hamiltoniano.")
else:
    print("O grafo não possui um Circuito Hamiltoniano.")
