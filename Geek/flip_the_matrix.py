def solution():
    N,K = map(int,input().split())
    ans = []
    s = 0
    for i in range(N):
        row = list(map(int, input().split()))
        ans.append(row)
    print(ans)
    for i in range(N):
        for j in range(N):
            s += ans[i][j]
    return max(s-K,0)
if __name__ == "__main__":
    for case in range(int(input())):
        print(solution())