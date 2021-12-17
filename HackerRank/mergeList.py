from math import factorial
for _ in range(int(input())):
    n,m=map(int,input().split())
    print(factorial(n+m)//factorial(n)//factorial(m)%(10**9+7))
