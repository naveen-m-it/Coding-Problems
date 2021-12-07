#Naveen 07-12-2021
def solve(s):
    n=0
    ans = []
    for i in range(len(s)):
        n=0
        count = 0
        while n<i:
            if s[i]>s[n]:
                count+=1
            n+=1
        ans.append(count)
    return ans



