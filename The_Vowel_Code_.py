def encode(s):
    letters = list(s)
    vowels = ['a','e','i','o','u']
    for i in range(0, len(letters)):
        if letters[i].lower() in vowels:
            letters[i] = str(vowels.index(letters[i].lower()) + 1)
        else:
            pass
    return ''.join(letters)
    
def decode(s):
    vowels_num = ['1','2','3','4','5']
    vowels = ['a','e','i','o','u']
    letters = list(s)
    for i in range(0, len(letters)):
        if letters[i] in vowels_num:
            letters[i] = vowels[int(letters[i]) - 1]
        else:
            pass
    return ''.join(letters)
