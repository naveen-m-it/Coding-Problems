"""
2
6
1 3 0 5 8 5
2 4 6 7 9 9
3
10 12 20
20 25 30

"""

#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        ans = 0
        arr=[] 
        for i in range(n):
            arr.append(start[i])
            arr.append(end[i])
            for j in range(n):
                if end[i]!=start[j] and end[i]<start[j]:
                    ans+=1
                    break

        # code here
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends