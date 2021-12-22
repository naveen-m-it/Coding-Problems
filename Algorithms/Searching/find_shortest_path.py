import sys
sys.setrecursionlimit(int(1e9+7))
def shortest_path(graph,start,end,path=[]):
    path = path+[start]
    if start==end:
        return path
    if not graph.__contains__(start):
        return None
    shortest=None
    for node in graph[start]:
        if node not in path:
            newPath = shortest_path(graph,node,end,path)
            if newPath:
                if not shortest or len(newPath) < len(shortest):
                    shortest = newPath
    return shortest
if __name__ == "__main__":
    graph = {
        'A':['B','C'],
        'B':['C','D'],
        'C':['D'],
        'D':['C'],
        'E':['F'],
        'F':['C']
    }
    ans = shortest_path(graph,'A','D')
    print('->'.join(ans)) if type(ans)==list else print(ans)