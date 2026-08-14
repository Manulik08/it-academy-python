print("Задание 1")
total_price = int(input("Введите сумму покупки: "))
client_type = input('Введите тип клиентской зоны ("RU", "EU" или "US"): ').upper()
if client_type == "RU":
    if total_price >= 5000:
        print("Доставка бесплатная")
    else:
        print("Доставка стоит 500 руб.")
        total_price += 500
elif client_type == "EU":
    print("Стоимость доставки 1000 руб. для любых заказов")
    total_price += 1000
elif client_type == "US":
    if total_price > 15000:
        print("Доставка стоит 800 руб.")
        total_price += 800
    else:
        print("Доставка стот 2000 руб.")
        total_price += 2000
print(f"Итоговая стоимость: {total_price=}")