n,m = map(int,input().split())
count = 0
for i in range(1,min(n,m)+1):
    if m%i==0 and n%i==0:
        count+=1
print(count)
