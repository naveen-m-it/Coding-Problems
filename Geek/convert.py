#User function Template for python3
class Solution:

	def convert(self,arr, n):
	    low = min( arr )
        ans = []
        sum = 0
        for i in range(n):
            a = arr[i]
            sum = (a%low)
	    return low
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.convert(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends