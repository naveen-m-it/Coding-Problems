
def swap(j,i,list):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def bubbleSort(list):
    n = len(list)
    while n > 1:
        i = 1
        while i < n:
            if list[i] < list[i - 1]:
                swap( i, i - 1,list)
            i += 1
        n -= 1
    return list

if __name__ == "__main__":
    list=[1,4,3,2,5]
    print(bubbleSort(list))
