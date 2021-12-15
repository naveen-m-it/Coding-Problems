t = int(input())
for i in range(t):
    n = int(input())
    prod = 1
    sum = 0
    for i in range(1,n+1):
        prod*=i
        sum+=i
    if prod%sum==0:
        print("YEAH")
    else:
        print("NAH")