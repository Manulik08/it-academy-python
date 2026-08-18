print("Задание 4")

cities = [
"Москва",
"Париж",
"Берлин",
"Рим",
"Токио"
]

filtered_cities = sorted(cities, key=lambda x: x[::-1])

print(filtered_cities)