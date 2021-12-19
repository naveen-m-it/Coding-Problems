def binarySearch(arr,x):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = low+(high-low)//2
        if arr[mid]==x:
            return True
        elif arr[mid]<x:
            low = mid+1
        else:
            high = mid-1
    return False

if __name__ == "__main__":
    arr = range(1,11)
    x = 10
    ans = binarySearch(arr,x)
    print(ans)