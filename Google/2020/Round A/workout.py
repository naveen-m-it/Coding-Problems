def solve(n,k,m):
    while k>0:
        
        k-=1
if __name__ == "__main__":
    for tc in range(int(input())):
        n,k = map(int,input().split())
        m = list(map(int,input().split(maxsplit=n)))
        ans = solve(n,k,m)
        print(f"Case# {tc+1}: {ans}")
