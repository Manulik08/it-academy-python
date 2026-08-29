print("Задание 2")

"""Создайте класс Car, описывающий автомобиль.Реализуйте 
приватные атрибуты для марки (__make), модели (__model) и 
пробега (__mileage). 
Добавьте геттер и сеттер для пробега.  
В сеттере проверьте условие: пробег не может быть 
отрицательным числом, а также не может уменьшаться 
(новый пробег должен быть больше или равен старому)."""

class Car:
    def __init__(self, make: str, model: str, mileage: int):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
    @property
    def car_mileage(self):
        return self.__mileage

    @car_mileage.setter
    def car_mileage(self, value):
        if value < 0:
            raise ValueError("пробег не может быть отрицательным числом")
        elif value < self.__mileage:
            raise ValueError("пробег не может уменьшаться")
        self.__mileage = value

    def __str__(self):
        return f"{self.__make} {self.__model}, пробег: {self.__mileage}"


car = Car(make= "BMW", model="X6", mileage= 40000)
print(car)
car.car_mileage = 45000
print(f"После увеличения: {car}")
car.car_mileage = -100

