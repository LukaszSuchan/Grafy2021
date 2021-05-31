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


    def minDistance(self, dist, sptSet):
        min = float('inf')
        min_index = None
        for v in range(self.vertices):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.vertices):
            print(node, "\t", dist[node])

    def dijkstra(self, src):

        dist = [float('inf')] * self.vertices
        dist[src] = 0
        sptSet = [False] * self.vertices

        for cout in range(self.vertices):

            u = self.minDistance(dist, sptSet)

            sptSet[u] = True
            for v in range(self.vertices):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)