print("Задание 2")

from functools import wraps

def ignore_duplicates(func):
    recurring = None
    recurring_set = set()
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal recurring
        for arg in args:
            if arg == recurring:
                return None
            recurring = arg

        for key, value in kwargs.items():
            if key and value in recurring_set:
                return None
            recurring_set.add({key: value})

        return func(*args, **kwargs)

    return wrapper


@ignore_duplicates
def send_message(text: str):
    print(f"Отправлено: {text}")


send_message("Привет")
send_message("Привет")
send_message("Как дела?")
send_message("Как дела?")
send_message("Привет")




