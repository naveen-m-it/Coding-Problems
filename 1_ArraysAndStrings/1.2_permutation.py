
# Naveen M
# 14-Nov-2021
# Python 3.9.7 64-bit(windows)

def permutation(str1,str2):
    if len(str1)!=len(str2):
        return False
    str1,str2 = list(str1),list(str2)
    str1.sort()
    str2.sort()
    return str1==str2
    