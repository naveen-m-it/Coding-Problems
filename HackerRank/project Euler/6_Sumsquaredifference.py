from math import sqrt
sqr = 0
su = 0
n=100
for i in range(1,n+1):
    sqr+=i*i
    su+=i
s=abs(sqr-(su*su))
print(s)