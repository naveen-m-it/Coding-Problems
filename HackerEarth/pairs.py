def pairs(k, arr):
    return len(set(arr) & set([item+k for item in set(arr)]))