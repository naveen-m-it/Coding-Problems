
def bubbleSort(arr):
    for i in range(len(arr)):
        already_s =True
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                already_s = False
        if already_s:
            break

if __name__ == "__main__":    
    arr=[16, 19, 20, 2, 9, 10, 3, 12, 11, 13, 15, 6, 7, 8, 1, 18, 17, 5, 14, 4]
    bubbleSort(arr)
    print(arr)
