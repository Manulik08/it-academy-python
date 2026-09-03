print("Задание 2")
"""Небольшое задание именно на наследование и 
переопределение методов. Создайте базовый класс: 
Notification. У него должен быть метод: send(message). 
Затем создайте: 
● EmailNotification; 
● SMSNotification; 
● PushNotification. 
Каждый класс должен по-своему реализовать send(). 
Проверить в цикле. 
Дополнительное усложнение: добавить в Notification общий 
атрибут recipient и использовать super().__init__() в дочерних 
классах."""

class Notification:
    def __init__(self, recipient):
        self.recipient = recipient

    def send(self, message):
        print(f"Для {self.recipient} отправлено следующее сообщение: {message}")

class EmailNotification(Notification):
    def __init__(self, recipient):
        super().__init__(recipient)

    def send(self, message):
        print(f"Для {self.recipient} на email отправлено следующее сообщение: {message}")

class SMSNotification(Notification):
    def __init__(self, recipient):
        super().__init__(recipient)

    def send(self, message):
        print(f"Для {self.recipient} на SMS отправлено следующее сообщение: {message}")

class PushNotification(Notification):
    def __init__(self, recipient):
        super().__init__(recipient)

    def send(self, message):
        print(f"Для {self.recipient} на Push отправлено следующее сообщение: {message}")

user_1 = EmailNotification(recipient= "Jake")
user_1.send(message="Hello!")

user_2 = SMSNotification(recipient="Max")
user_2.send(message="How are you?")

user_3 = PushNotification(recipient="Jess")
user_3.send("What are you doing this evening?")



