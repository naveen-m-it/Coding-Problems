def MonkAndInversions(n,m):
    count=0
    for i in range(n):
        for j in range(n):
            for p in range(n):
                for q in range(n):
                    if i<=p and j<=q:
                        if m[i][j]>m[p][q]:
                            count+=1
    return count
if __name__ == "__main__":
    for tc in range(int(input())):
        n = int(input())
        m = []
        for i in range(n):
            r = list(map(int,input().split()))
            m.append(r)
        ans = MonkAndInversions(n,m)
        print(ans)