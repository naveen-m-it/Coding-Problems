#Naveen M
def printPascal(n):
    c = 1
    for i in range(1,n+2):
        print (c%(10**9),end=" "),
        c = c * (n+1-i)//i
    print()
for t in range(int(input())):
    printPascal(int(input()))