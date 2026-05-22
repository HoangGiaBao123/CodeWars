def disemvowel(string):
    vowels = ["o", "u", "i", "e", "a"]
    chars = [c for c in string if c.lower() not in vowels]
    return "".join(chars)
