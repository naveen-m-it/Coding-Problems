#naveen m
def solve(n,m):
    temp = 0
    res = [1]
    for i in range(1,n+1):
        s = i-m-1
        e = i-1
        if s>=0:
            temp-=res[s]
        temp+=res[e]
        res.append(temp)
    return res[n]
if __name__ == "__main__":
    n = int(input())
    m = 2
    ans = solve(n,m)
    print(ans)
