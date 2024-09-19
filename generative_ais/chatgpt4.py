import random

def generate_hamiltonian_cycle(n):
    # Cria uma lista de nós
    nodes = list(range(n))
    
    # Embaralha os nós para gerar uma permutação aleatória
    random.shuffle(nodes)
    
    # Cria o ciclo conectando cada nó ao próximo
    cycle = [(nodes[i], nodes[(i + 1) % n]) for i in range(n)]
    
    return cycle

def hamiltonian_cycle(graph):
    def is_valid_vertex(v, pos, path):
        # Checa se é adjacente ao último vértice no caminho atual
        if graph[path[pos - 1]][v] == 0:
            return False

        # Checa se o vértice já foi incluído no caminho
        if v in path:
            return False

        return True

    def ham_cycle_util(path, pos):
        # Se todos os vértices estão incluídos no caminho
        if pos == len(graph):
            # E se há uma aresta do último ao primeiro vértice
            return graph[path[pos - 1]][path[0]] == 1

        for v in range(1, len(graph)):
            if is_valid_vertex(v, pos, path):
                path[pos] = v
                if ham_cycle_util(path, pos + 1):
                    return True
                path[pos] = -1

        return False

    path = [-1] * len(graph)
    path[0] = 0

    if not ham_cycle_util(path, 1):
        return None
    path.append(path[0])
    return path

# Exemplo de uso
graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

cycle = hamiltonian_cycle(graph)
if cycle:
    print("Circuito Hamiltoniano encontrado:", cycle)
else:
    print("Nenhum circuito Hamiltoniano encontrado.")