print("Задание 1")

while True:
    message = input("Введите cообщение: ")
    if message.lower() == "exit":
        print("Сервер выключен")
        break
    with open("log.txt","a",encoding="utf-8") as file:
        file.write(message + "\n")
    print("Сообщение сохранено")