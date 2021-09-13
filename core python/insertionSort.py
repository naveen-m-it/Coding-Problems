
"""  Hello! This is Naveen                 """
"""  https://www.github.com/naveen-m-it    """

#insertion sort
def insertionSort(list):
    i = 1
    while i < len(list):
        itemToInsert = list[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < list[j]:
                list[j + 1] = list[j]
                j -= 1
            else:
                break
        list[j + 1] = itemToInsert
        i += 1
    return list
#main method
if __name__ == "__main__":
    list = [1,4,3,2,5]
    print(insertionSort(list))