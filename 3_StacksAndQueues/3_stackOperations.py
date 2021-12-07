class Stack:

    def __init__(self) -> None:
        self.stack = []

    def push(self,element):
        if type(element) is int:
            self.stack.insert(0,element)
            return
        if type(element) is list:
            for i in range(len(element)):
                self.stack.insert(0,element[-(i+1)])
        return

    def pop(self):
        if len(self.stack)==0:
            print("No elements in the stack\n")
            return
        po = self.stack.pop(0)
        print(po,"poped from stack")
        print()
        return
    
    def min(self):
        if len(self.stack)==0:
            print("Stack has no elements")
            print()
            return
        a = min(self.stack)
        print("min is",a)
        print()
        return

    def print(self):
        print(self.stack)
        print()
        return

    def size(self):
        print("size of the stack is",len(self.stack))
        print()
        return

    def isEmpty(self):
        a = True if len(self.stack)==0 else False
        if a:
            print("stack is empty")
        else:
            print("stack is not empty")
        return

stack = Stack()
if __name__ == "__main__":
    print("==========Stack function========")
    exit = False
    while exit!=True:
        operation = input(
        "pop     - pop and delete top of the stack element\n"
        "push    - add new element top of the stack\n"
        "print   - print stack elements\n"
        "size    - return size of the stack\n"
        "isEmpty - return stack empty or not\n"
        "min     - return min element of the stack\n"
        "exit    - leave\n"
        ">>>")
        try:
            if operation == "push":
                x = int(input("Enter element: "))
                stack.push(x)
                print(f"{x} add top of the stack\n")
            elif operation == "pop":
                stack.pop()
            elif operation == "print":
                stack.print()
            elif operation == "size":
                stack.size()
            elif operation == "isEmpty":
                stack.isEmpty()
            elif operation == "min":
                stack.min()
            elif operation == "exit":
                exit = True
            else:
                print(f"stack has no command '{operation}'\nplease enter valid command")
        except:
            print("Value error: 'Please enter valid input'")