#Naveen M
def confusingNumber(n):
    dic = {'1':'1','0':'0','8':'8','9':'6','6':'9'}
    ro_str = ""
    ntr = str(n)
    for c in ntr[::-1]:
        if c not in dic:
            return False
        else:
            ro_str+=dic[c]
    return ro_str!=ntr
def solve(n):
    count = 0
    for i in range(n+1):
        ans = confusingNumber(i)
        if ans:
            count+=1
    return count
if __name__ == "__main__":
    n = int(input())
    ans = solve(n)
    print(ans)