print("Задание 5")

import csv
import re

with open("data.csv","w",encoding="utf-8") as file:
    file.write("name,email,phone\n")
    file.write("Alex,alex@example.com,+375291234567\n")
    file.write("Maria,maria@test.by,+375441112233\n")
    file.write("John,john@example,+375123\n")
    file.write("Anna,anna@gmail.com,+375297788979\n")

email_pattern = r'\w+@\w+\.\w+'
phone_pattern = r'\+\d{12}'
invalid_users = []
with open ("data.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['name']
        email = row['email']
        phone = row['phone']

        is_email =re.search(email_pattern,email)
        is_phone = re.search(phone_pattern,phone)

        if not is_email or not is_phone:
          invalid_users.append({"name":name,
                              "email":email,
                              "phone":phone,
                              "is_email":bool(is_email),
                              "is_phone":bool(is_phone),
                              })

print("Пользователи с некорректными данными:")
if not invalid_users:
    print("Все пользователи с корректными данными ")
else:
    for i in invalid_users:
        print(f"Имя:{i['name']}")
        if not i["is_email"]:
            print(f"Некорректный email:{i['email']}")
        if not i["is_phone"]:
            print(f"Некорректный номер:{i['phone']}")