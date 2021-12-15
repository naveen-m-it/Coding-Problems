class Solution:
    def querySum(self, n, arr, q, queries):
        ans = []
        for i in range(0,len(queries)-1,2):
            low = queries[i]
            high = queries[i+1]
            count=0
            for i in range(low-1,high):
                count+=arr[i]
            ans.append(count)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input().split()
        for i in range(n):
            arr[i] = int(arr[i])
        q = int(input())
        queries = input().split()
        for i in range(0,2*q,2):
            queries[i] = int(queries[i])
            queries[i+1] = int(queries[i+1])
        
        ob = Solution()
        ans = ob.querySum(n, arr, q, queries)
        for it in(ans):
            print(it,end=" ")
        print()
# } Driver Code Ends