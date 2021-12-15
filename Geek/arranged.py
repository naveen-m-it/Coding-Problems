#User function Template for python3



class Solution:
    def arranged(self,a,n):
        arr1 = []
        arr2 = []
        ans = []
        for i in range(n):
            if a[i]<0:
                arr2.append(a[i])
            else:
                arr1.append(a[i])
        for i in range(len(arr1)):
            ans.append(arr1[i])
            ans.append(arr2[i])
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=Solution().arranged(a,n)
    print(*ans)

# } Driver Code Ends