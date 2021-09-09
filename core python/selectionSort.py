
"""  Hello! This is Naveen                 """
"""  https://www.github.com/naveen-m-it    """

#selection sort function
def selectionSort(list):
    i = 0
    while i < len(list)-1:
        minIndex = i
        j = i+1
        while j<len(list):#search method
            if list[j]<list[minIndex]:
                minIndex = j
            j+=1
        if minIndex != i:
            swap(minIndex,i,list)#swap method
        i+=1
    return list
#swap tow elements in a list using temp method
def swap(j,i,list):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
#main method
if __name__ == "__main__":
    list = [1,4,3,2,5,7,6,9,8]
    print(selectionSort(list))