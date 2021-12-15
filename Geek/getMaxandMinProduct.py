#User function Template for python3

def getMaxandMinProduct( A, Q, N, M):
    ans = []
    for i in range(M):
        count = 0
        for j in range(N):
            if Q[i]==0:
                count=0
                break
            if A[j]%Q[i]==0:
                count+=1
        ans.append(count)
    return ans
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, m = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        brr = [int(x) for x in input().strip().split()]
        
        ans = getMaxandMinProduct( arr, brr, n, m)
        for i in ans:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends