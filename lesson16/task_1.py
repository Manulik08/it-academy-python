print("Задание 1")
"""Создайте класс BankAccount, который представляет 
банковский счёт. У объекта должны быть: 
owner — имя владельца; _balance — текущий баланс. 
Реализуйте методы: 
● deposit(amount) — пополнение счёта; 
● withdraw(amount) — снятие денег; 
● get_balance() — получение текущего баланса. 
Правила: 
● нельзя пополнить счёт на отрицательную или нулевую 
сумму; 
● нельзя снять отрицательную или нулевую сумму; 
● нельзя снять больше денег, чем есть на счёте. 
Замените get_balance() на property, чтобы баланс можно 
было получать так:"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Нельзя пополнить счёт на отрицательную или нулевую сумму")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Нельзя снять отрицательную или нулевую сумму")
        if amount > self._balance:
            raise ValueError("Нельзя снять больше денег, чем есть на счёте")
        self._balance -= amount


user = BankAccount(owner="Aleks", balance=1000)
print(user.get_balance)

user.deposit(100)
print(user.get_balance)

user.withdraw(500)
print(user.get_balance)