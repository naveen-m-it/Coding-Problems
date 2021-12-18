# Naveen M
import math
def primefactors(n):
    ans = []
    while n % 2 == 0:
        ans.append(2),
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while (n % i == 0):
            ans.append(i)
            n = n / i
    if n > 2:
        ans.append(n)
    return max(ans)
n = 600851475143
ans = primefactors(n)
print(ans)
