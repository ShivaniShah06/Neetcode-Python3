# Date: June 6th 2024 ##
# Breadth First Search is a graph traversal method.

##################### Examples ######################
# Input: graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}. We call function with vertex 2 as the starting point of the traversal
# Output: 2, 0, 3, 1
#####################################################
# Solution reference: https://www.youtube.com/watch?v=U5-bRX2AHNY, https://www.geeksforgeeks.org/python-program-for-breadth-first-search-or-bfs-for-a-graph/
# Summary of solution: 
#####################################################

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self, s):
        print("\n")
        visited = []
        queue = []

        queue.append(s)
        visited.append(s)

        while queue:
            s = queue.pop(0)

            print(s, end=" ")

            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)

# Calling the function

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.BFS(2)
g.BFS(1)

g1 = Graph()
g1.addEdge(5,3)
g1.addEdge(5,7)
g1.addEdge(3,2)
g1.addEdge(3,4)
g1.addEdge(7,8)
g1.addEdge(4,8)
g1.BFS(5)
