#Naveen 07-12-2021
def solve(s,k):
    ans = []
    for i in range(len(s)):
        ans.append(s)
        s = s[1:]
    ans.sort()
    return ans[k-1]
