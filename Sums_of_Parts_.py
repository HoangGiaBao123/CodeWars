def parts_sums(ls):
    arr = ls
    total = 0
    sums = []
    for n in range (1, len(arr) + 2):
        if arr != []:
            total = sum(arr)
            sums.append(total)
            arr.pop(0)
        else:
            sums.append(0)
            break
    return sums
