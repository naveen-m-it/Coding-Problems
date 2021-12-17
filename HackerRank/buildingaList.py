#Naveen M
from itertools import combinations
def solve(s):
    s = list(s)
    lis = []
    for i in range(1,len(s)+1):
        a = list(combinations(s,i))
        lis.extend(a)
    lis.sort()
    for i in range(len(lis)):
        print(''.join(list(lis[i])))
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        s = input()
        solve(s)