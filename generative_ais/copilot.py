class Graph:
    def __init__(self, vertices):
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.V = vertices

    def is_safe(self, v, pos, path):
        if self.graph[path[pos - 1]][v] == 0:
            return False
        if v in path:
            return False
        return True

    def hamiltonian_cycle_util(self, path, pos):
        if pos == self.V:
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False

        for v in range(1, self.V):
            if self.is_safe(v, pos, path):
                path[pos] = v
                if self.hamiltonian_cycle_util(path, pos + 1):
                    return True
                path[pos] = -1
        return False

    def hamiltonian_cycle(self):
        path = [-1] * self.V
        path[0] = 0

        if not self.hamiltonian_cycle_util(path, 1):
            print("Não existe um circuito Hamiltoniano")
            return False

        self.print_solution(path)
        return True

    def print_solution(self, path):
        print("Circuito Hamiltoniano existe: ", end="")
        for vertex in path:
            print(vertex, end=" ")
        print(path[0], "\n")

# Exemplo de uso
g = Graph(5)
g.graph = [[0, 1, 0, 1, 0],
           [1, 0, 1, 1, 1],
           [0, 1, 0, 0, 1],
           [1, 1, 0, 0, 1],
           [0, 1, 1, 1, 0]]

g.hamiltonian_cycle()
