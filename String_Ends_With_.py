def solution(text, ending):
    if text.endswith(ending):
        return True
    else:
        return False

  if __name__ == '__main__':
    print(solution("Hello, my friends!", "!"))
