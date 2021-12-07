
# Naveen M ( naveen_m_it | Github ) 
# 15-Nov-2021
# Python 3.9.7 64-bit(windows)

def nullifyRow(mat,row):
    for j in range(len(mat)):
        mat[row][j]=0

def nullifyCol(mat,col):
    for i in range(len(mat)):
        mat[i][col]=0

def setZero(mat):
    rowHasZero = False
    colHasZero = False
    for j in range(len(mat[0])):
        if mat[0][j]==0:
            rowHasZero = True
            break
    for i in range(len(mat)):
        if mat[i][0]==0:
            colHasZero = True
            break
    for i in range(1,len(mat)):
        for j in range(1,len(mat[0])):
            if mat[i][j]==0:
                mat[i][0]=0
                mat[0][j]=0
    for i in range(len(mat)):
        if mat[i][0]==0:
            nullifyRow(mat,i)
    for j in range(len(mat[0])):
        if mat[0][j]==0:
            nullifyCol(mat,j)
    if rowHasZero:
        nullifyRow(mat,0)
    if colHasZero:
        nullifyCol(mat,0)
    return mat
