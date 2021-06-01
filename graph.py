import json
import numpy as np

class Graph():
    def __init__(self):
        self.graph = []
        self.vertices = 0

    def load(self, filename):
        try:
            file = open(filename)
        except:
            return "Invalid file path"
        try:
            data = json.load(file)
        except:
            return "Error while parsing JSON"

        matrix = []
        for i in range(len(data)):
            matrix.append([0] * len(data))
            for j in data[i]:
                matrix[i][j] = 1
        self.graph = matrix
        self.vertices = len(matrix)

    def minDistance(self, dist, queue):

        minimum = float("Inf")
        min_index = -1

        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index


    def printPath(self, parent, j):
        if parent[j] == -1:
            print(j, end=' ')
            return
        self.printPath(parent, parent[j])
        print(j , end=' ')

    def printSolution(self, dist, parent):
        src = 0
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(1, len(dist)):
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i]),end=''),
            self.printPath(parent, i)

    def dijkstra(self, graph, src):

        row = len(graph)
        col = len(graph[0])
        dist = [float("Inf")] * row
        parent = [-1] * row
        dist[src] = 0

        queue = []
        for i in range(row):
            queue.append(i)

        while queue:

            u = self.minDistance(dist, queue)
            queue.remove(u)
            for i in range(col):
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u

        self.printSolution(dist, parent)