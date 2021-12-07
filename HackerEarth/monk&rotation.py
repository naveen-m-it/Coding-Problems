def MonkAndRotation(n,k,a):
    if n==k or k==0:
        print(*a)
    elif n>k:
        i = n-k
        print(*a[i:],*a[:i])
    else:
        i = n-(k%n)
        print(*a[i:],*a[:i])
for i in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    MonkAndRotation(n,k,a)