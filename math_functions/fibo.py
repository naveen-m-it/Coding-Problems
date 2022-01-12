def fibo(n):
    arr = [0,1]
    for i in range(n):
        arr.append(arr[i]+arr[i+1])
    return arr[:n]
