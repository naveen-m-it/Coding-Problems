def solve(n,k,p,pile):
    sum = 0
    plates = p
    while plates>0:
        a = 0
        for i in range(k):
            if len(pile[i])!=0:
                a=i
                break
        value = s = pile[a][0]
        for i in range(n):
            if len(pile[i])!=0 and value<pile[i][0]:
                value=pile[i][0]
                ind = i
        if value==s:
            value = pile[a].pop(0)
        else:
            value = pile[ind].pop(0)
        sum+=value
        plates-=1
    return sum

if __name__ == "__main__":
    for tc in range(int(input())):
        n,k,p = map(int,input().split())
        pile = []
        for i in range(n):
            stack = list(map(int,input().split()))
            pile.append(stack)
        ans = solve(n,k,p,pile)
        print(f"Case #{tc+1}: {ans}")
