#User function Template for python3

def getCandidate(n, k):
    max1 = 1
    for i in range(n):
        l = pow(k,i)
        max1 = max(max1,l)
        if n<max1:
            return pow(k,i-1)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        
        print(getCandidate(n, k))
# } Driver Code Ends