
# Naveen M ( naveen_m_it | Github ) 
# 15-Nov-2021
# Python 3.9.7 64-bit(windows)

def compressBad(str1):
    compressedString = ""
    count = 0
    for i in range(len(str1)):
        count+=1
        if i+1>=len(str1) or str1[i]!=str1[i+1]:
            compressedString+=str1[i]+str(count)
            count=0
    return compressedString if len(compressedString)<len(str1) else str1
