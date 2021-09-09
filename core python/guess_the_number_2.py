
"""  Hello! This is Naveen                 """
"""  https://www.github.com/naveen-m-it    """

#in this function computer will guess the number

import random
def main():
    low = int(input("starting number:"))
    high = int(input("ending number:"))
    user_input = None
    steps=0
    while user_input!="=":
        computer_choice = random.randint(low,high)
        print("Your number is:",computer_choice)
        user_input = input("Enter = OR < OR >: ")
        steps+=1
        if user_input=="<":
            high=computer_choice-1
        elif user_input==">":
            low=computer_choice+1
    print(f"I got the number in {steps} tries!")
if __name__=="__main__":
    main()
