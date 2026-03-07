import math

def get_average(marks):
    total = 0
  
    for m in marks:
        total += m
    return math.floor(total / len(marks))
