
def fact(n):
    if n==0 or n==1:
        return n
    return n+fact(n-1)
if __name__ == "__main__":
    print(fact(10))