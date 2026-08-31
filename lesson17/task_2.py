print("Задание 2")
"""Разработайте систему отправки уведомлений 
пользователям. 
1. Создайте общий базовый интерфейс для уведомлений. 
Отправка сообщения должна выполняться через 
единый метод. 
2. Реализуйте отдельные классы для: 
○ Email; 
○ SMS; 
○ Push. 
3. Каждый способ отправки должен иметь собственное 
поведение. 
4. Создайте функцию, которая получает список 
уведомлений и отправляет через них одно сообщение. 
Функция должна работать с разными типами 
уведомлений через полиморфизм, без проверки 
конкретного класса объекта. 
5. Добавьте возможность создавать уведомление 
альтернативным способом из конфигурации, например 
из словаря с настройками получателя. 
6. Добавьте статический метод для проверки 
корректности данных получателя. 
7. Создайте собственную иерархию исключений для 
ошибок системы уведомлений. Предусмотрите как 
минимум: 
○ некорректного получателя; 
○ ошибку отправки уведомления. 
8. Реализуйте __str__(), чтобы объекты уведомлений 
имели понятное строковое представление."""


class NotificationError(Exception):
    pass

class InvalidRecipientError(NotificationError):
    pass

class SendError(NotificationError):
    pass



class Notification:
    def __init__(self, recipient):
        if not recipient:
            raise InvalidRecipientError("Получатель не может быть пустой строкой")
        self.recipient = recipient

    def send(self, message):
        print(f"Сообщение для {self.recipient}: {message}")

    def __str__(self):
        return f"{self.__class__.__name__}: {self.recipient}"

    @staticmethod
    def is_valid_notification(recipient, notification_type):
        if not recipient:
            return False

        if notification_type == "email":
            return "@" in recipient
        elif notification_type == "sms":
            return recipient.startswith("+") and len(recipient) >= 13
        elif notification_type == "push":
            return len(recipient) >= 5
        else:
            return False
    @classmethod
    def from_config(cls, config):
        notification_type = config.get("type")
        recipient = config.get("recipient")

        if not notification_type or not recipient:
            raise InvalidRecipientError("Отсутствие полей 'type' и 'recipient'")

        if not cls.is_valid_notification(recipient, notification_type):
            raise InvalidRecipientError("Некорректные данные")

        if notification_type == "email":
            return EmailNotification(recipient)
        elif notification_type == "sms":
            return SMSNotification(recipient)
        elif notification_type == "push":
            return PushNotification(recipient)
        else:
            raise InvalidRecipientError("Неизвестный тип уведомления")


class EmailNotification(Notification):
    def __init__(self, recipient):
        super().__init__(recipient)

    def send(self, message):
        if not "@" in self.recipient:
            raise InvalidRecipientError("Некорректный email")
        print(f"Сообщение для {self.recipient} отправлено на email: {message}")


class SMSNotification(Notification):
    def __init__(self, recipient):
        super().__init__(recipient)

    def send(self, message):
        if not self.recipient.startswith("+") or len(self.recipient) < 13:
            raise InvalidRecipientError("Некорректный номер")
        print(f"Сообщение для {self.recipient} отправлено в sms: {message}")


class PushNotification(Notification):
    def __init__(self, recipient):
        super().__init__(recipient)

    def send(self, message):
        if len(self.recipient) < 5:
            raise InvalidRecipientError("Некорректный ID")
        print(f"Сообщение для {self.recipient} отправлено push: {message}")



def all_send(notifications, message):
    for notification in notifications:
        try:
            notification.send(message)
        except InvalidRecipientError as e:
            print(f"️Ошибка при отправке {notification}: {e}")


notifications_us = [
    EmailNotification("user@mail.com"),
    EmailNotification("usermail.com"),
    SMSNotification("+375291234567"),
    PushNotification("device_123")
]
all_send(notifications_us, message="Привет!")


configs = [
    {"type": "email", "recipient": "user@mail.com"},
    {"type": "sms", "recipient": "+375299876543"},
    {"type": "push", "recipient": "device_123"},
    {"type": "email", "recipient": "bad"},
    {"type": "sms", "recipient": "123"}
]

notifications = []
for config in configs:
    try:
        notification = Notification.from_config(config)
        notifications.append(notification)
    except InvalidRecipientError as e:
        print(f"Не удалось создать уведомление: {e}")
print(f"Создано {len(notifications)} уведомлений из {len(configs)} конфигураций")
all_send(notifications, "Уведомление")