#Naveen M
#4613732
num = [1,2]
i = 0
sum=0
while True:
    if 4_000_000>num[i]+num[i+1]:
        if (num[i]+num[i+1])%2==0:
            sum+=num[i]+num[i+1]
        num.append(num[i]+num[i+1])
    else:
        break
    i+=1
print(sum+2)
