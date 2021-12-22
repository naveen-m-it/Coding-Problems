# path finding algorithm
def find_path(graph,start,end,path=[]):
    path.append(start)
    if start==end:
        return path
    if not graph.__contains__(start):
        return None
    for node in graph[start]:
        if node not in path:
            newPath = find_path(graph,node,end)
            if newPath:
                return newPath
    return None
if __name__ == "__main__":
    graph = {
        'A':['B','C'],
        'B':['C','D'],
        'C':['D'],
        'D':['E'],
        'E':['F'],
        'F':['C']
    }
    ans = find_path(graph,'A','D')
    print('->'.join(ans)) if type(ans)==list else print(ans)
            