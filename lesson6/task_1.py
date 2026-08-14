from random import randint
print("Задание 1")
print("Угадайте загаданное число, у вас есть 5 попыток!")
random_number = randint(1,50)
for i in range(5):
    user_number = int(input("Введите ваше число: "))
    if random_number == user_number:
        print("Поздравляю! Вы угадали загаданное число!")
        break
    elif user_number < random_number:
        print("Больше!")
    else:
        print("Меньше!")
else:
    print(f"Попытки закончились. Загаданное число было: {random_number}")
print("Игра окончена")