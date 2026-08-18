print("Задание 2")

try:
    user_input_balance = float(input("Введите баланс счёта: "))
    user_input_transfer = float(input("Введите сумму перевода: "))

    if user_input_transfer > user_input_balance:
        print("Ошибка: сумма перевода больше баланса ")
    else:
        balance = user_input_balance + user_input_transfer
        print("Операция проведена успешно")
        print(f"Теперь ваш баланс составляет: {balance}")
except ValueError:
    print("Некорректно введенные данные")
finally:
    print("Операция завершена")