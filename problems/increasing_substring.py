
"""  Hello! This is Naveen                 """
"""  https://www.github.com/naveen-m-it    """
"""
Problem:
Your friend John just came back from vacation, and he would like to share with you a new property that 
he learned about strings. John learned that a string C of length L consisting of uppercase English characters 
is strictly increasing if, for every pair of indices i and j such that 1≤i<j≤L (1-based), the character at 
position i is smaller than the character at position j. For example, the strings ABC and ADF are strictly 
increasing, however the strings ACC and FDA are not. Now that he taught you this new exciting property, 
John decided to challenge you: given a string S of length N, you have to find out, for every position 1≤i≤N, 
what is the length of the longest strictly increasing substring that ends at position i.

###Input###
-----------
The first line of the input gives the number of test cases, T. T test cases follow.
Each test case consists of two lines.
The first line contains an integer N, representing the length of the string.
The second line contains a string S of length N, consisting of uppercase English characters.

###Output###
------------
For each test case, output one line containing Case #x: y1 y2 ... yn, where x is the test case number (starting from 1) 
and yi is the length of the longest strictly increasing substring that ends at position i.
Limits
Memory limit: 1 GB.
1≤T≤100.
Test Set 1
Time limit: 20 seconds.
1≤N≤100.
Test Set 2
Time limit: 40 seconds.
1≤N≤2×105.

Sample Inputs:      Sample Outputs:
2                   Case #1: 1 2 1 2
4                   Case #2: 1 2 1 2 3 1
ABBC
6
ABACDA

"""
def increasing_substring():
    N = int(input())
    S = input()
    ans = [1]*N
    for i in range(1, N):
        if S[i-1] < S[i]:
            ans[i] = ans[i-1]+1
    return " ".join(map(str, ans))
if __name__ == "__main__":
    for case in range(int(input())):
        print ("Case #%d: %s" % (case+1, increasing_substring()))