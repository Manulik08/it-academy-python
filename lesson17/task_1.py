print("Задание 1")
"""Базовый класс Order. У заказа должны быть: 
● номер; 
● сумма; 
● статус. 
Реализуйте методы: 
● pay() 
● cancel() 
Заказ нельзя отменить после оплаты. Если пользователь 
пытается выполнить недопустимую операцию, должно 
возникать собственное исключение: InvalidOrderStateError. 
Создайте иерархию: 
OrderError 
└── InvalidOrderStateError 
● Добавьте __str__:  Объект заказа должен красиво 
отображаться: Заказ #1001: 250 EUR, статус: оплачено 
● Добавьте __eq__:Два заказа считаются одинаковыми, 
если у них одинаковый номер."""

class OrderError(Exception):
    pass

class InvalidOrderStateError(OrderError):
    pass


class Order:
    def __init__(self, number, summa, status):
        self.number = number
        self.summa = summa
        self.status = status

    def pay(self):
        if self.status == "оплачено":
            raise InvalidOrderStateError("Ваш заказ уже оплачен")
        elif self.status == "отменено":
            raise InvalidOrderStateError("Нельзя оплатить отмененный заказ")
        self.status = "оплачено"

    def cancel(self):
        if self.status == "отменено":
            raise InvalidOrderStateError("Ваш заказ уже отменен")
        elif self.status == "оплачено":
            raise InvalidOrderStateError("Нельзя отменить оплаченный заказ")
        self.status = "отменено"

    def __str__(self):
        return f"Заказ {self.number}: {self.summa} EUR, статус: {self.status}"

    def __eq__(self, other):
        return self.number == other.number


order_1 = Order(number="#1010", summa=100, status="поступивший")
print(order_1)
order_1.pay()
print(order_1)
# order_1.cancel()

order_2 = Order(number="#1011", summa=200, status="оплачено")
print(order_2)
# order_2.cancel()
# order_2.pay()

order_3 = Order(number="#1011", summa=350, status="отменено")
print(order_3)
# order_3.pay()

order_4 = Order(number="#1012", summa=500, status="поступивший")
print(order_4)
order_4.cancel()
print(order_4)

print(order_2 == order_3)





# zakaz = Order(number=320, summa=5000, status="поступивший")
# print(zakaz.get_order)
# zakaz.pay()
# print(zakaz.get_order)



