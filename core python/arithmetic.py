x = int(input("enter a number"))
y = int(input("enter a number"))
z = input("enter a arithmetic symbol")

if(z=='+'):
    print(x+y)

elif(z=='-'):
    print(abs(x-y))

elif(z=='*'):
    print(x*y)

elif(z=='/'):
    print(x/y)

else:
    print("Please enter valid input")