# Depth First Search
from collections import defaultdict
class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfsUtil(self,v,visited,path=[]):
        visited.add(v)
        print(v,end=' ')
        for n in self.graph[v]:
            if n not in visited:
                self.dfsUtil(n,visited)
    
    def dfs(self,s):
        visited=set()
        self.dfsUtil(s,visited)
