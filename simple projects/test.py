#Binary Search(Iterative)
def binarySearch(arr,x):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (high+low)//2
        if x==arr[mid]:
            return True
        elif x>arr[mid]:
            low = mid+1
        else:
            high = mid-1
    return False


