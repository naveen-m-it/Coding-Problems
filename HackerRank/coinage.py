#Naveen M
def f(n,x,i,z,dp):
    if n==0:return 1
    if i>3 :return 0
    if (n,i) in dp:return dp[n,i]
    ans=0
    for j in range(x[i]+1):
        if n-j*z[i]<0:break
        ans+=f(n-j*z[i],x,i+1,z,dp)
    dp[n,i]=ans
    return ans
def solve(n, x):
    z=(1,2,5,10)
    return f(n,x,0,z,{})
if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        coins = list(map(int, input().rstrip().split()))
        result = solve(n, coins)
        print(result)
