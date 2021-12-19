# Linear Search
def linearSearch(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return True
    return False

if __name__ == "__main__":
    arr = [int(i) for i in range(1,11)]
    x = 11
    ans = linearSearch(arr,x)
    print(ans)