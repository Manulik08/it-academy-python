print("Формулы:")

def square(number: int | float):
    return number ** 2

def cube(number: int | float):
    return number ** 3

def is_even(number: int | float):
    if number % 2 == 0:
        return True
    else:
        return False

def factorial(number: int | float):
    if number <= 1:
        return 1
    return number * factorial(number - 1)

def max_of_two(a: int | float, b: int | float):
    if a > b:
        return a
    else:
        return b