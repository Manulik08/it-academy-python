print("Задание 1")
temperature = int(input("Введите текущую температуру воздуха на улице: "))
if temperature < -10:
    print("Холодно, наденьте куртку")
elif -10 <= temperature <= 15:
    print("Прохладно, оденьтесь теплее")
else:
    print("Тепло, можно идти в футболке")

