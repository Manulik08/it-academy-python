print("Задание 1")
name = input("Введите свое имя: ")
print(name)
weight = float(input("Введите свой вес (в кг): "))
print(weight)
height = float(input("Введит свой рост: "))
print(height)
bmi = weight / height ** 2
print("Исходя из введенных данных ваш ИМТ составляет:", int(bmi))
