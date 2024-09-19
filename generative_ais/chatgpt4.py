def is_hamiltonian_cycle(graph, path, pos):
    # Verifica se todos os vértices estão incluídos no caminho
    if pos == len(graph):
        # Verifica se existe uma aresta entre o último e o primeiro vértice
        return graph[path[pos - 1]][path[0]] == 1

    # Tenta diferentes vértices como próximo candidato no caminho Hamiltoniano
    for v in range(1, len(graph)):
        if is_safe(v, graph, path, pos):
            path[pos] = v

            # Recurre para construir o resto do caminho
            if is_hamiltonian_cycle(graph, path, pos + 1):
                return True

            # Remove o vértice atual se não leva a uma solução
            path[pos] = -1

    return False

def is_safe(v, graph, path, pos):
    # Verifica se este vértice é adjacente ao anterior
    if graph[path[pos - 1]][v] == 0:
        return False

    # Verifica se o vértice já foi incluído
    if v in path:
        return False

    return True

def hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0  # Começa do primeiro vértice

    if is_hamiltonian_cycle(graph, path, 1):
        return path + [path[0]]  # Retorna o caminho com ciclo fechado
    else:
        return None

# Exemplo de uso
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

cycle = hamiltonian_cycle(graph)
if cycle:
    print("Circuito Hamiltoniano encontrado:", cycle)
else:
    print("Nenhum Circuito Hamiltoniano existe")