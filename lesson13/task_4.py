print("Задание 4")

items = []

while True:
    command = input("Введите команду: ").lower()
    try:

        if command == "add":
            number_input = int(input("Введите число которое хотите обавить в список: "))
            items.append(number_input)

        elif command == "remove":
            index_input = int(input("Введите индекс числа которое хотите удалить из списка: "))
            items.pop(index_input)

        elif command == "show":
            print(items)

        elif command == "exit":
            break

        else:
            print("Некорректная команда")
    except ValueError:
        print("Некорректные данные ввода. Введите число.")

    except  IndexError:
        print("Вы ввели некорректный индекс.")

