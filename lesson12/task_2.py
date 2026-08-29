print("Задание 2")
from functools import wraps
def limit_calls(limit, message, default = None):
    def decorator_limit_calls(func):
        count = 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal count
            if count < limit:
                count += 1
                return func(*args, **kwargs)
            else:
                print(message)
                return default
        return wrapper
    return decorator_limit_calls

@limit_calls(2, "Лимит!", 0)
def add(a, b):
    return a + b

print(add(1, 2))
print(add(2, 3))
print(add(5, 8))
print(add(6, 4))

@limit_calls(3, "Больше нельзя!", [])
def get_items(category):
    return ["item1", "item2"]

print(get_items("Apple"))
print(get_items("Cucumber"))
print(get_items("Lemon"))
print(get_items("Pear"))
print(get_items("Tomato"))

