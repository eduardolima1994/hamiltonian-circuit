import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

def create_graph(adjacency_matrix):
    G = nx.Graph()
    size = len(adjacency_matrix)
    edge_count = 0
    for i in range(size):
        for j in range(i + 1, size):
            if adjacency_matrix[i][j] != 0:
                G.add_edge(i, j, label=chr(97 + edge_count))
                edge_count += 1
    return G

def find_hamiltonian_cycle(G):
    nodes = list(G.nodes)
    for perm in permutations(nodes):
        if all(G.has_edge(perm[i], perm[i+1]) for i in range(len(perm) - 1)) and G.has_edge(perm[-1], perm[0]):
            return perm + (perm[0],)
    return None

def draw_graph(G, cycle=None):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')
    
    labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    if cycle:
        edge_list = [(cycle[i], cycle[i+1]) for i in range(len(cycle) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color='r', width=2)
    
    plt.show()

adjacency_matrix = [
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0]
]


graph = create_graph(adjacency_matrix)
cycle = find_hamiltonian_cycle(graph)

if cycle:
    print("Hamiltonian cycle found:", cycle)
else:
    print("No Hamiltonian cycle found.")

draw_graph(graph, cycle)
