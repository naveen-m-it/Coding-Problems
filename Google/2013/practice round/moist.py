if __name__ == "__main__":
    t = int(input())
    for x in range(1,t+1):
        n = int(input())
        names = [input() for index in range(n)]
        y = 0
        previous = names[0]
        for name in names[1:]:
            if name<previous:
                y+=1
            else:
                previous = name
        print(f"Case #{x}: {y}",flush=True) 