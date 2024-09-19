# Função para verificar se um vértice pode ser adicionado ao caminho
def is_safe(v, graph, path, pos):
    # Verifica se o vértice é adjacente ao último vértice adicionado
    if graph[path[pos - 1]][v] == 0:
        return False
    
    # Verifica se o vértice já foi incluído no caminho
    if v in path:
        return False

    return True

# Função para encontrar o Circuito Hamiltoniano usando backtracking
def hamiltonian_cycle_util(graph, path, pos):
    # Se todos os vértices foram incluídos no caminho
    if pos == len(graph):
        # Verifica se há uma aresta do último vértice ao primeiro
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    # Tenta adicionar os vértices ao ciclo
    for v in range(1, len(graph)):
        if is_safe(v, graph, path, pos):
            path[pos] = v

            # Recursão para verificar o próximo vértice
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True

            # Se adicionar o vértice v não leva a uma solução, remove-o (backtracking)
            path[pos] = -1

    return False

# Função para resolver o problema do Circuito Hamiltoniano
def hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    
    # Começa o ciclo no vértice 0
    path[0] = 0

    if not hamiltonian_cycle_util(graph, path, 1):
        print("Nenhum Circuito Hamiltoniano encontrado.")
        return False

    # Imprime o ciclo encontrado
    print("Circuito Hamiltoniano encontrado:", path + [path[0]])
    return True

# Exemplo de grafo representado por uma matriz de adjacência
graph = [[0, 1, 0, 1, 0],
         [1, 0, 1, 1, 1],
         [0, 1, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [0, 1, 1, 1, 0]]

# Executa o algoritmo
hamiltonian_cycle(graph)
