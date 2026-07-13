# Three types of graph
"""
1-Directed Graph
2-Undirected Graph
3-Weighted Graph
"""

class Graph:
    def __init__(self,vertex):
        self.matrix = [[0 for i in range(vertex)] for i in range(vertex)]
        self.size = vertex

    # Undirected Graph
    def add_edge(self,src,dest):
        if(0 <= src < self.size and 0<=dest<self.size):
            self.matrix[src][dest] = 1
            self.matrix[dest][src] = 1
        else:
            print("Invalid edge")

    def print(self):
        for row in self.matrix:
            print(' '.join(map(str,row)))

graph = Graph(5)
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(3,4)
graph.add_edge(2,3)
graph.print()
