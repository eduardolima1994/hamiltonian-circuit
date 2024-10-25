import random

def create_non_hamiltonian_graph(size=37):
    # Inicializar a matriz com zeros
    adjacency_matrix = [[0 for _ in range(size)] for _ in range(size)]
    
    # Definir padrões de ciclos locais sem ligação de todos os vértices
    for i in range(size - 1):
        # Conectar o vértice i com i+1 para criar um ciclo parcial
        adjacency_matrix[i][i + 1] = 1
        adjacency_matrix[i + 1][i] = 1

    # Criar algumas ligações adicionais para ciclos sem fechar o caminho
    for i in range(0, size - 2, 4):
        if i + 2 < size:
            adjacency_matrix[i][i + 2] = 1
            adjacency_matrix[i + 2][i] = 1

    # Adicionar arestas aleatórias para criar mais ciclos locais
    for _ in range(size // 2):
        v1, v2 = random.randint(0, size - 1), random.randint(0, size - 1)
        if v1 != v2:
            adjacency_matrix[v1][v2] = 1
            adjacency_matrix[v2][v1] = 1

    return adjacency_matrix

# Gerar a matriz
adjacency_matrix = create_non_hamiltonian_graph()

# Formatação para o padrão de saída desejado
print("adjacency_matrix = [")
for i, row in enumerate(adjacency_matrix):
    print(f"    {row},  # {i}")
print("]")
