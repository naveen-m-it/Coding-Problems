
# Naveen M
# 15-Nov-2021
# Python 3.9.7 64-bit(windows)

def oneEditAway(str1, str2):
    if len(str1) == len(str2):
        return oneEditReplace(str1, str2)
    elif len(str1)+1 == len(str2):
        return oneEditInsert(str1, str2)
    elif len(str1)-1 == len(str2):
        return oneEditInsert(str2, str1)
    return False

def oneEditReplace(str1, str2):
    dif = False
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            if dif:
                return False
            dif = True
    return True

def oneEditInsert(str1, str2):
    i1 = 0
    i2 = 0
    while i2<len(str2) and i1<len(str1):
        if str1[i1]!=str2[i2]:
            if i1!=i2:
                return False
            i2+=1
        else:
            i1+=1
            i2+=1
    return True 

