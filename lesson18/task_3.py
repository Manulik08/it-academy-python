print("Задание 3")
"""Есть интернет-магазин. 
Сейчас существуют три вида скидки: 
● обычная — 5%; 
● постоянный клиент — 10%; 
● VIP — 20%. 
Нужно реализовать расчёт скидки. 
Главное условие 
Код расчёта заказа не должен содержать конструкцию: 
if discount_type == . 
для каждого нового типа скидки. 
Добавьте возможность легко создать новую стратегию 
скидки. 
Усложнение 
Добавьте: 
● скидку на день рождения; 
● скидку по промокоду. 
При этом существующий код расчёта заказа менять не 
должен."""


# class StandardDelivery:
#     def calculate(self, price):
#         return 10
# class ExpressDelivery:
#     def calculate(self, price):
#         return 30
# class Order:
#     def __init__(self, delivery_strategy):
#         self.delivery_strategy = delivery_strategy
#     def delivery_cost(self, price):
#         return self.delivery_strategy.calculate(price)
#
#
# order = Order(StandardDelivery())
# print(order.delivery_cost(100))
# order = Order(ExpressDelivery())
# print(order.delivery_cost(100))


class DefaultDiscount:
    def discount(self, prise):
        return prise * 0.95

class RegularDiscount:
    def discount(self, prise):
        return prise * 0.90

class VIPDiscount:
    def discount(self, prise):
        return prise * 0.80

class BirthdayDiscount:
    def discount(self, prise):
        return prise * 0.85

class PromoDiscount:
    def __init__(self, promocod):
        self.promocod = promocod
        cods = ["SUMMER", "AUTUMN", "WINTER", "SPRING"]
        if self.promocod not in cods:
            raise ValueError("Введен некорректный промокод")

    def discount(self, prise):
        return prise * 0.85



class Discount:
    def __init__(self, discount_strategy):
        self.discount_strategy = discount_strategy
    def discount_cost(self, price):
        return self.discount_strategy.discount(price)


default = Discount(discount_strategy=DefaultDiscount())
print(default.discount_cost(100))

default2 = Discount(discount_strategy=PromoDiscount(promocod="SUMMER"))
print(default2.discount_cost(100))

# default2 = Discount(discount_strategy=PromoDiscount(promocod="SUMMERRRR"))
# print(default2.discount_cost(100))




