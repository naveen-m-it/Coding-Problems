def insertionSort(list):
    i = 1
    while i < len(list):
        itemToInsert = list[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < list[j]:
                list[j + 1] = list[j]
                j -= 1
            else:
                break
        list[j + 1] = itemToInsert
        i += 1
    return list

if __name__ == "__main__":
    import random
    list = [x for x in range(1_00_000)]
    random.shuffle(list)
    print(list)
    print(insertionSort(list))