#User function Template for python3

class Solution:
    def countPairs(self,arr1, arr2, M, N, x):
        ans=0
        for i in range(M):
            for j in range(N):
                if arr1[i]+arr2[j]==x:
                    ans+=1
        return ans
                    


#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    m,n=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x=int(input())
    ob = Solution()
    print(ob.countPairs(a,b,m,n,x))


# } Driver Code Ends