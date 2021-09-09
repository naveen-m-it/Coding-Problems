
"""  Hello! This is Naveen                 """
"""  https://www.github.com/naveen-m-it    """

#in this function user will guess the number

import random
def main():
    low = int(input("starting number:"))
    high = int(input("ending number:"))
    computer_choice = random.randint(low,high)
    user_input=0
    steps=0
    while user_input!=computer_choice:
        steps+=1
        user_input = int(input("Guess the number: "))
        if user_input<computer_choice:
            print("Too low")
        elif user_input>computer_choice:
            print("Too high")
    print(f"You got the number {computer_choice} in {steps} tries!")
if __name__=="__main__":
    main()
