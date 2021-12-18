s = 1000
for a in range(1,s//3):
    for b in range(s//2):
        c = s-a-b
        if a*a+b*b==c*c:
            print(a*b*c)
