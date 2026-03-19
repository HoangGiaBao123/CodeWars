def array_diff(a, b):
    setted = set(b)
    if a == []:
        return []
    elif b == []:
        return a
    else:
        for n in setted:
            while n in a:
                a.remove(n)
    return a
