print("Задание 2")
file = input(f"Введите имя файла: ")
size_file = int(input("Введите размер файла: "))
admin = True if (input("Являетесь ли вы администратором? (yes/no): ").lower()) == "yes" else False
ends_no = ('.exe', '.bat')
ends_yes = ('.zip', '.rar')
if file.endswith(ends_no) and admin == False:
    print("Доступ запрещен: опасный файл")
elif file.endswith(ends_yes) and size_file < 100 and admin == True:
    print("Архив администратора принят")
else:
    print("Файл отправлен на проверку")