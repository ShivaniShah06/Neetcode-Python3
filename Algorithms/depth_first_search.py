# Date: June 9th 2024 ##
# Depth First Search is a graph traversal method.
# DFS explores each child before exploring the node itself. There are three traversal methods based on when you add the
# print statement:
#   1. Preorder traversal: Vertex, Left, Right
#   2. Inorder traversal: Left, Vertex, Right
#   3. Postorder traversal: Left, Right, Vertex

##################### Examples ######################
# Input: graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}. We call function with vertex 2 as the starting point of the traversal
# Output: 2 0 1 3
#####################################################
# Solution reference: https://www.geeksforgeeks.org/python-program-for-depth-first-search-or-dfs-for-a-graph/, https://www.youtube.com/watch?v=Sbciimd09h4
# Summary of solution: 
#####################################################
from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUtil(self, v, visited):

        visited.add(v)
        print(v, end =" ")

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
    
    def DFS(self, v):
        visited = set()

        self.DFSUtil(v, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFS(2)
