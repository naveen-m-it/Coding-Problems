from collections import defaultdict
class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def bfs(self,s,path=[]):
        visited = [False]*(max(self.graph)+1)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            path.append(s)
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
        return path