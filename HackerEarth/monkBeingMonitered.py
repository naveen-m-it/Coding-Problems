#NaveenM 07-12-2021
import sys
def solve(n,arr):
    dic = {}
    for i in arr:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    mini,maxi = sys.maxsize,-sys.maxsize-1
    for j,i in sorted(dic.items()):
        mini = min(i,mini)
        maxi = max(i,maxi)
    if maxi-mini<=0:
        return -1
    else:
        return maxi-mini
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        ans = solve(n,arr)
        print(ans)
