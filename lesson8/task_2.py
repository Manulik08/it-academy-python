print("Задание 2")
def business_card(name, surname, **kwargs):
    print("=====================")
    print(f"{name} {surname}")
    print()

    for kwarg in sorted(kwargs):
        print(f"{kwarg.capitalize()}: {kwargs[kwarg]}")

    print("=====================")

business_card(name="Ivan", surname="Ivanov", age=30, city="Минск", company="Google", email="ivan@gmail.com")


