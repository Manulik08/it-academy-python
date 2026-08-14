print("Задание 3")
password = "Python2026"
i = 5
while i > 0:
    user_password = input("Введите пароль: ")
    if user_password == password:
        print("Доступ разрешён")
        break
    elif user_password == "exit":
        break
    else:
        i -= 1
        print(f"Пароль неверный. У вас осталось {i} попыток.")
else:
    print("Аккаунт заблокирован")