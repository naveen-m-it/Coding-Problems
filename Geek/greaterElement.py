#User function Template for python3


def greaterElement (arr,  n) : 
    #Complete the function
    return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = greaterElement(arr, n);
    ans = ""
    for i in res:
        if(i == -10000000):
            ans += "_ "
        else:
            ans += str(i)
    print(ans)



# } Driver Code Ends