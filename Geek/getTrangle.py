
def getTriangle( arr, n):
    final_ans=arr[::-1]
    while len(arr)>1:
        curr_ans=[]
        for i in range(len(arr)-1):
            curr_ans.append(arr[i]+arr[i+1])
        final_ans.extend(curr_ans[::-1])
        arr=curr_ans
    return final_ans[::-1]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        Triangle = getTriangle(a, n)
        print(*Triangle)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends