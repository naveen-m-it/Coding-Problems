
"""  Hello! This is Naveen                 """
"""  https://www.github.com/naveen-m-it    """

# Binary Search
def binarySearch(item, list):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if item == list[mid]:
            return "Item found in the list at position-",mid+1
        elif item < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

if __name__=="__main__":
    # you can use user input list
    #list = list(map(int,(input("enter numbers: ")).split()))
    
    # here I use pre defined list
    list = [1,2,3,4,6,7,8,24,76,12,-21]
    # binary search only work with sorted list
    list.sort()
    item = int(input("Enter search item: "))
    if binarySearch(item,list)==-1:
        print("Item not Found in the List")
    else:
        print(binarySearch(item,list))

