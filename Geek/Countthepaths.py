def possible_paths(graph, n, s, d):
        ans = 0
        if s == d:
            return 1
        for x in graph:
            if x[0] == s:
                ans += possible_paths(graph, n, x[1], d)
        return ans