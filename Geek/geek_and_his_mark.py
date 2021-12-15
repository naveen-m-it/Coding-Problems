def solution():
    N,X = map(int,input().split())
    arr = list(map(int,input().split(maxsplit=N)))
    ans = 0
    for i in range(N):
        if arr[i]>X:
            ans+=1
    return ans

if __name__ == "__main__":
    for case in range(int(input())):
        print(solution())