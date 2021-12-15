#User function Template for python3

def game_with_number (arr,  n) :
    ans = []
    for i in range(n):
        if i==n-1:
            ans.append(arr[i])
            return ans
        ans.append(arr[i]^arr[i+1])

#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = game_with_number(arr, n);
    print(*res)




# } Driver Code Ends