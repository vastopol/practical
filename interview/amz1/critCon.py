from collections import defaultdict

class Graph:
    def __init__(self, verticies):
        self.V = verticies + 1
        self.adj_list = defaultdict(list)
        self.parent = [-1] * self.V
        self.low = [float('inf')] * self.V
        self.disc = [float('inf')] * self.V
        self.visited = [False] * self.V
        self.time = 0
        self.con = 0

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def find_cons(self, u):
        self.visited[u] = True
        self.low[u] = self.time
        self.disc[u] = self.time
        self.time += 1
        for v in  self.adj_list[u]:
            if not self.visited[v]:
                self.parent[v] = u
                self.find_cons(v)
                self.low[u] = min(self.low[u], self.low[v])
                if self.low[v] > self.disc[u]:
                    self.con.append([u,v])
            elif v != self.parent[u]:
                self.low[u] = min(self.low[u], self.disc[v])

    def criticalConnection(numOfServers, numOfConnections, connections):
        try:
            g = Graph(numOfServers)
            for c in connections:
                g.add_edge(c[0], c[1])
            for j in range(1, g.V):
                if not g.visited[j]:
                    g.find_cons(j)
            critical = g.con
        except:
            critical = list()
        return sorted(critical)



