def subMatrixSum(self,arr, n, m, x1, y1, x2, y2):
    sum = 0
    for i in range(x1-1,x2):
            for j in range(y1-1,y2):
	            sum+=arr[i][j]
    return sum