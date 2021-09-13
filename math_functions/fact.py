
"""  Hello! This is Naveen                 """
"""  https://www.github.com/naveen-m-it    """

#recursive function
def fact(n):
    if n==0 or n==1:
        return n
    #fact(n) = n+(n-1)+...+n=0
    return n+fact(n-1)
if __name__ == "__main__":
    print(fact(10))