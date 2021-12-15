def solution():
    N = int(input())
    return ((N//10) + ((N%10)//5) +(((N%10)%5)//2) + (((N%10)%5)%2))
if __name__ == "__main__":
    for case in range(int(input())):
        print(solution())