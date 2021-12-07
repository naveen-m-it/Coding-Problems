
# Naveen M
# 15-Nov-2021
# Python 3.9.7 64-bit(windows)

def rotate(mat):
    if len(mat)==0 or len(mat)!=len(mat[0]):
        return False
    n = len(mat)
    for layer in range(n//2):
        first = layer
        last = n-1-layer
        for i in range(first,last):
            offset = i-first
            top  = mat[first][i]
            mat[first][i] = mat[last-offset][first]
            mat[last-offset][first] = mat[last][last - offset]
            mat[last][last - offset] = mat[i][last]
            mat[i][last] = top
    return mat
