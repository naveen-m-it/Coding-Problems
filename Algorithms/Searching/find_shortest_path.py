# finding shortest path using stacks
def shortest_path_1(graph,start,end,path=[]):
    path = path+[start]
    if start==end:
        return path
    if not graph.__contains__(start):
        return None
    shortest=None
    for node in graph[start]:
        if node not in path:
            newPath = shortest_path_1(graph,node,end,path)
            if newPath:
                if not shortest or len(newPath) < len(shortest):
                    shortest = newPath
    return shortest

# finding shortest path using queue
from collections import deque
def shortest_path_2(grpah,start,end):
    dist = {start:[start]}
    q = deque(start)
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at],next]
                q.append(next)
    return dist.get(end)
    
if __name__ == "__main__":
    graph = {
        'A':['B','C'],
        'B':['C','D'],
        'C':['D'],
        'D':['C'],
        'E':['F'],
        'F':['C']
    }
    ans = shortest_path_1(graph,'D','C')
    print(ans)