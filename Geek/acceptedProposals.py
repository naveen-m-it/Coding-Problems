#User function Template for python3

class Solution:
    def acceptedProposals (self,arr, n):
        arr.sort()
        return arr[n-2],arr[1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    arr = list(map(int, input().split()))
    ob = Solution()
    res = ob.acceptedProposals (arr, n)
    print (res[0], end = " ")
    print (res[1])
# } Driver Code Ends