def solution():
    n,k = map(int,input().split())
    for i in range(k):
        if(n%10 == 0):
            return n
        n = n ^ (n % 10)
    return n
for case in range(int(input())):
    print("%d"%solution())