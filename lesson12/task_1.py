print("Задание 1")
from functools import wraps
def repeat(times, separator):
    def repeat_separator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(str(func(*args, **kwargs)))

            return ("\n" + separator + "\n").join(results)
        return wrapper
    return repeat_separator


@repeat(times=3, separator="---")
def greet(name):
    return f"Привет, {name}!"
print(greet("Иван")) 

@repeat(times=2, separator="=")
def add(a, b):
    return a + b
print(add(5, 3))




