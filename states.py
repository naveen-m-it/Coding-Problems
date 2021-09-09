
"""  Hello! This is Naveen                 """
"""  https://www.github.com/naveen-m-it    """

def mean(input):
    file = (input.split())
    avg = 0
    for i in file:
        avg = avg+int(i)
    print("Avarage is  :",(avg/len(file)))
def main(input):
    file = input.split()
    call = []
    index = len(call)//2
    for i in file:
        call.append(int(i))
    print("the List is :",call)
    index = len(call)//2
    call.sort()
    print("Mediun is   :",call[index])
    mean(input)
if __name__=="__main__":
    """here input is list"""
    input = (input())
    main(input)
