#User function Template for python3

class Solution:
	def minimum_difference(self, nums):
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-1):
            ans.append(abs(nums[i]-nums[i+1]))
        return (min(ans))

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.minimum_difference(nums)
		print(ans)
# } Driver Code Ends