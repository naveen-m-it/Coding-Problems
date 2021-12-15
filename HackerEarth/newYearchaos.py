
def minimumBribes(q):
    briebs = [0]*len(q)
    while sorted(q)!=q:
        for i in range(len(q)-1):
            n = len(q)-i-1
            temp = 0
            if q[n]<q[n-1]:
                temp = q[n]
                q[n] = q[n-1]
                q[n-1] = temp
                briebs[q[n]-1]+=1
    if max(briebs)>2:
        return "Too chaotic"
    else:
        return sum(briebs)
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
