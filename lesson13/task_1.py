print("Задание 1")

while True:
    user_input = input("Введите число от 1 до 100: ")
    if user_input == "exit":
        break

    try:
        user_number = int(user_input)

        if user_number < 0 or user_number > 100:
            print("Ошибка: введенное число не входит в диапазон")
        else:
            print(f"Число принято: {user_number}")
            break

    except ValueError:
        print("Ошибка: необходимо ввести число")

