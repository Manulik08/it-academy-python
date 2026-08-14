print("Задание 2")
print("Способ 1")
city = input("Введите ваш город: ")
city_1 = city[0:3]
city_2 = city[-3:]
summ = city_1 + city_2
print(summ, summ, summ, sep="-")

print("Способ 2")
city = input("Введите ваш город: ")
city_1 = city[0:3]
city_2 = city[-3:]
summ = city_1 + city_2
print("-".join([summ] * 3))
