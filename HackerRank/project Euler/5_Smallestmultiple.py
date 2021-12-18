# Naveen M
from functools import reduce 
from math import gcd
n = 20
print(reduce(lambda x,y: x*y//gcd(x,y), range(1,n+1)))