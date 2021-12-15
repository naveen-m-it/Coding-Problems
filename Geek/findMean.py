#User function Template for python3

class Solution:  
    def findMean(self, arr, queries, n, q): 
        ans = []
        for i in range(0,q,2):
            l = queries[i]
            r = queries[i+1]
            s = 0           
            count = 0
            for j in range(l,r+1):
                s += arr[j]
                count+=1
            ans.append(s//count)      
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3
    
for _ in range(0,int(input())):
    n,q = map(int,input().strip().split())
    arr = list(map(int,input().strip().split()))
    queries = list(map(int,input().strip().split()))
    ob=Solution()
    v = ob.findMean(arr, queries, n, 2*q)
    print(*v)
    
# } Driver Code Ends