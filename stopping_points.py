import networkx as nx
import matplotlib.pyplot as plt

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

def print_graph_and_matrix(graph, cycle):
    G = nx.Graph()
    
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] == 1:
                G.add_edge(i, j)
    
    edge_labels = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    all_edges = list(G.edges())
    for idx, edge in enumerate(all_edges):
        edge_labels[edge] = alphabet[idx % len(alphabet)]
    
    print("Graph:")
    for edge in all_edges:
        print(f"{edge[0]}-{edge[1]} : {edge_labels[edge]}")
    
    if cycle:
        n = len(graph)
        cycle_matrix = [[0] * n for _ in range(n)]
        for i in range(len(cycle) - 1):
            cycle_matrix[cycle[i]][cycle[i+1]] = 1
            cycle_matrix[cycle[i+1]][cycle[i]] = 1
        cycle_matrix[cycle[-1]][cycle[0]] = 1
        cycle_matrix[cycle[0]][cycle[-1]] = 1
        
        print("\nAdjacency Matrix:\n[")
        for row in cycle_matrix:
            print("    " + str(row) + ",")
        print("]\n")

def draw_graph_and_cycle(graph, cycle):
    G = nx.Graph()
    
    for i in range(len(graph)):
        for j in range(i+1, len(graph)):
            if graph[i][j] == 1:
                G.add_edge(i, j)
    
    pos = nx.spring_layout(G)
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    
    edge_labels = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    all_edges = list(G.edges())
    for idx, edge in enumerate(all_edges):
        edge_labels[edge] = alphabet[idx % len(alphabet)]
    
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')
    
    if cycle:
        edges_in_cycle = [(cycle[i], cycle[i+1]) for i in range(len(cycle) - 1)] + [(cycle[-1], cycle[0])]
        
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_cycle, edge_color='r', width=2)
    
    plt.title("Grafo e Ciclo Hamiltoniano (se encontrado)")
    plt.show()


adjacency_matrix = [
    [0, 0, 0, 1, 1],
    [0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0]
]

cycle = find_hamiltonian_cycle(adjacency_matrix)
if cycle:
    print_graph_and_matrix(adjacency_matrix, cycle)
    print("Hamiltonian Cycle found:\n", cycle)
    draw_graph_and_cycle(adjacency_matrix, cycle)
else:
    print("No Hamiltonian Cycle found")
    draw_graph_and_cycle(adjacency_matrix, None)