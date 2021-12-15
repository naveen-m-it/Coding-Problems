#User function Template for python3
class Solution:
    def sort(self, s): 
        arr = list(s)
        arr.sort()
        ans = ""
        for i in arr:
            ans+=i
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        obj = Solution()
        ans = obj.sort(s)
        print(ans)
# } Driver Code Ends