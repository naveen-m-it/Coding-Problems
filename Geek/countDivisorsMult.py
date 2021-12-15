#User function Template for python3

class Solution:
    def countDivisorsMult(self, a, n):
        count = 1
        ans=0
        for i in range(n):
            count*=a[i]
        for i in range(1,count+1):
            if count%i==0:
                ans+=1
        return ans
    
    
    
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        print(Solution().countDivisorsMult(a, n))
        
        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends