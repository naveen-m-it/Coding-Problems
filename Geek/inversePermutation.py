#User function Template for python3

def inversePermutation (arr, n) :
    ans= []
    for i in range(n):
        n=arr[i]
        ans.insert(i,n)
    return ans 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

    
for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = inversePermutation(arr, n)
    print(*ans)
    





# } Driver Code Ends