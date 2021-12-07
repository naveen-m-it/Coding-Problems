# Naveen M
# 23-11-2021-Tue-05:56:PM
def solve(n,k,a):
    p = -1
    big = ""
    for i in range(n):
        if big < a:
            big = a
            d = i
        elif big == a:
            p = i - d
            break
        a = a[1:] + a[:1]
    if p == -1:
        return ( d + ( k - 1 ) * n )
    return ( d + ( k - 1 ) * p )

if __name__ == "__main__":
    t = int(input())
    for tc in range(t):
        n,k = map(int,input().split())
        a = input()
        ans = solve(n,k,a)
        print(ans)