x =int(input("Enter first value:"))
y =int(input("Enter second valye:"))
print("\n1.Addition\n2.Substraction\n3.multiple\n4.divide")
c=int(input("Enter your choise"))
if c<2:
    d=x+y
    print("Addition of",x,"and",y,"is",d)
elif c<3:
    d=x-y
    print(abs(d))
elif c<4:
    d=x*y
    print(d)
elif c<5:
    d=x/y
    print(d)
else:
    print("you entered wrong input")
