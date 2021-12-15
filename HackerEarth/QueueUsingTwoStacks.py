from collections import deque
list1 = deque()
q = int(input())
while q>0:
    a = input()
    a = list(a.split())
    n = int(a[0])
    if len(a)==2:
        m = int(a[1])
    if n==1:
        list1.append(m)
    elif n==2:
        list1.popleft()
    elif n==3:
        print(list1[0])
    q-=1