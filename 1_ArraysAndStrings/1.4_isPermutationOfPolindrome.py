
# Naveen M
# 15-Nov-2021
# Python 3.9.7 64-bit(windows)

def isPermutationOfPolindrome(str):
    count = 0 
    table = [0]*256
    for i in str:
        x = ord(i)
        if x!=-1:
            table[x]+=1
            if table[x]%2==1:
                count+=1
            else:
                count-=1
    return count<=1
    