def first_non_repeating_letter(s):
    init_str = s
    strs = list(s.lower())
    non_repeat = ""
    for i in range (0, len(strs)):
        if strs.count(strs[i]) == 1:
            non_repeat = init_str[i]
            break
    return non_repeat
