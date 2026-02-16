def find_position(letter):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  letter_index = alphabet.index(letter) + 1
  return f'Position of the letter: {letter_index}'

if __name__ == '__main__':
  print(find_position(a)) # Position of the letter: 1
