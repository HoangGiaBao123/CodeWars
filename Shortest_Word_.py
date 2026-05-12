def find_short(string):
    words = string.split(" ")
    words_len = [len(word) for word in words]
    return min(words_len)
