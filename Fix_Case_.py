def solve(s):
    length = len(s)
    lowercase = [letter for letter in s if letter.islower()]
    different = length - len(lowercase)
    if different < len(lowercase):
        return s.lower()
    elif different > len(lowercase):
        return s.upper()
    else:
        return s.lower()
