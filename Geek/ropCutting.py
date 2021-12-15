#User function Template for python3

class Solution:
    def RopeCutting (self, arr, n) :
        arr.sort()
        res=[]
        for i in range(n-1):
            if(arr[i]!=arr[i+1]):
                res.append(n-i-1)
        return res
#{ 
#  Driver Code Starts
#Initial Template for Python 3

  
for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.RopeCutting(arr, n)
    print(*res)






# } Driver Code Ends