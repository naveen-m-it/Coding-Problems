#User function Template for python3

class Solution:
    def smallestDifferenceTriplet(self,a,b,c,n):
        
        return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ob = Solution()
    ans=ob.smallestDifferenceTriplet(a,b,c,n)
    print(ans[0],ans[1],ans[2])

# } Driver Code Ends