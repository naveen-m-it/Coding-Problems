def solve(n,b,arr):
    arr.sort()
    sum = 0
    for i in range(n):
        if arr[i]<=b:
            sum+=1
            b-=arr[i]
        else:
            return sum
if __name__ == "__main__":
    for tc in range(int(input())):
        n,b = map(int,input().split())
        arr = list(map(int,input().split()))
        ans = solve(n,b,arr)
        print(f"Case# {tc+1}: {ans}")