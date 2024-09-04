def is_safe(v, pos, path, graph):
    if graph[path[pos - 1]][v] == 0:
        return False

    if v in path:
        return False

    return True

def hamiltonian_cycle_util(graph, path, pos):
    if pos == len(graph):
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    for v in range(1, len(graph)):
        if is_safe(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            path[pos] = -1

    return False

def find_hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0  

    if not hamiltonian_cycle_util(graph, path, 1):
        return None
    return path

adjacency_matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

cycle = find_hamiltonian_cycle(adjacency_matrix)
if cycle:
    print("Hamiltonian Cycle found:", cycle)
else:
    print("No Hamiltonian Cycle found")