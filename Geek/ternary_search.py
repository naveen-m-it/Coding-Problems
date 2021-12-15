
def ternary_search(N,arr,K):
    return (ternary_search(arr,arr+N,K) != arr+N) ? 1 : -1 

if __name__ =="__main__":
    N = 9
    K = 5
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(ternary_search(N,arr,K))