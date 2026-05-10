def to_camel_case(text):
    words = text.replace("-", "_").split("_")
    for i in range(1, len(words)):
        words[i] = words[i].capitalize()
    return "".join(words)
