
# Naveen M
# 14-Nov-2021
# Python 3.9.7 64-bit(windows)

def isUnique(str):
    if len(str)>128:
        return False
    char_set = [False]*128
    for i in range(len(str)):
        val = ord(str[i])
        if char_set[val]:
            return False
        char_set[val] = True
    return True
