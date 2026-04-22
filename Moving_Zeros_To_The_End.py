def move_zeros(arr):
    zeros = [zero for zero in arr if zero == 0]
    no_zero = [num for num in arr if num != 0]
    return no_zero + zeros
