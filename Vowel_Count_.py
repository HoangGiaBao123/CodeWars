def get_count(sentence):
    if sentence.strip() != "":
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_count = [c for c in sentence if c in vowels]
        return len(vowel_count)
    else:
        return 0
