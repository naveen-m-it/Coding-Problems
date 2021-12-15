#Naveen M
def superDigit(n, k):
    if k==len(n)==1:
        return int(n)
    res = 0
    for i in n:
        res+=int(i)
    return superDigit(str(res*k),1)