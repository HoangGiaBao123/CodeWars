def count(s):
    obj = {}
    if s != '':
        for letter in s:
            obj.update({f'{letter}': s.count(letter)})
        return obj
    else:
        return {}
