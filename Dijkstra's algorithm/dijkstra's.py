
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node, distance in enumerate(dist):
            print(node, "\t\t", distance)

    def minDistance(self, dist, sptSet):
        min_dist = float('inf')
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_dist and not sptSet[v]:
                min_dist = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if (
                        self.graph[u][v] > 0
                        and not sptSet[v]
                        and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)


g = Graph(4)  # Adjust the graph size to match the adjacency matrix dimensions
g.graph = [
    [0, 8, 9, 2],
    [8, 0, 2, 0],
    [9, 2, 0, 2],
    [2, 0, 2, 0]
]
g.dijkstra(0)