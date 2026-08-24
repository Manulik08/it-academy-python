print("Задание 2")

import os
if not os.path.exists("data.txt"):
    print("Файл data.txt не существует")
else:
    with open ("data.txt","r",encoding="utf-8") as file:
        text = file.read()
    if not os.path.exists("backup"):
       os.makedirs("backup")
    with open("backup/data.txt","w",encoding="utf-8")as file:
        file.write(text)