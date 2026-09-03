print("Задание 3")
from functools import wraps

def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("Ошибка: деление на ноль.")
        except ValueError:
            print("Ошибка: некорректное значение.")

    return wrapper


@handle_errors
def divide(a, b):
    return a / b

print(divide(10, 5))
print(divide(10, 2))
print(divide(10, 0))


@handle_errors
def convert_to_int(value):
    return int(value)

print(convert_to_int("100"))
print(convert_to_int("hello"))



