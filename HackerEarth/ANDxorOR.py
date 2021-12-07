#Naveen 23-11-2021
def ANDxorOR(n,a):
    a.sort()
    min = (a[0] and a[1])^(a[0] or a[1])
    for i in range(n-1):
        j = i+1
        if min > (a[i] and a[j])^(a[i] or a[j]):
            min =  (a[i] and a[j])^(a[i] or a[j])
    return min
if __name__ == "__main__":
    t = int(input())
    for tc in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        ans = ANDxorOR(n,a)
        print(ans)