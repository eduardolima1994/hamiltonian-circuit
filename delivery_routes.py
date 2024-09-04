def is_safe(v, pos, path, graph):
    # Check if this vertex is an adjacent vertex of the previously added vertex.
    if graph[path[pos - 1]][v] == 0:
        return False

    # Check if the vertex has already been included.
    if v in path:
        return False

    return True

def hamiltonian_cycle_util(graph, path, pos):
    if pos == len(graph):
        # If there is an edge from the last vertex to the first vertex
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    for v in range(1, len(graph)):
        if is_safe(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            # Remove current vertex if it doesn't lead to a solution
            path[pos] = -1

    return False

def find_hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0  # Start at the first vertex

    if not hamiltonian_cycle_util(graph, path, 1):
        return None
    return path

# Example graph represented as an adjacency matrix
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

cycle = find_hamiltonian_cycle(graph)
if cycle:
    print("Hamiltonian Cycle found:", cycle)
else:
    print("No Hamiltonian Cycle found")