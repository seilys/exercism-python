MAX_SQUARES = 65

def square(number):
    if number not in range(1, MAX_SQUARES):
        raise ValueError("square must be between 1 and 64")
    return pow(2, number - 1)

def total():
    total = 0
    for i in range(1, MAX_SQUARES):
        total += square(i)
    return total
