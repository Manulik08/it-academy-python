print("Задание 3")
"""Создайте класс Item, представляющий предмет в инвентаре 
персонажа. 
Каждый предмет имеет: 
● name — название; 
● weight — вес; 
● price — стоимость. 
Необходимо перегрузить операторы: 
● + — объединяет два предмета в «набор» и возвращает 
их общую стоимость; 
● < — сравнивает предметы по весу; 
● == — считает предметы одинаковыми, если совпадают 
их названия; 
● str() — выводит предмет в удобном формате.
Дополнительное усложнение(необязательно) 
Добавьте класс Inventory и перегрузите оператор +, чтобы 
можно было написать: 
inventory + sword 
и получить новый инвентарь, содержащий исходные 
предметы и меч."""


class Bundl:
    def __init__(self, items):
        self.items = items
    @property
    def items_prise(self):
        return sum(item.prise for item in self.items)

    @property
    def items_weight(self):
        return sum(item.weight for item in self.items)

    def __str__(self):
        items_str = ", ".join(item.name for item in self.items)
        return f"Набор [{items_str}] — стоимость: {self.items_prise},  вес: {self.items_weight}"

class Item:
    def __init__(self, name, weight, prise):
        self.name = name
        self.weight = weight
        self.prise = prise

    def __add__(self, other):
        return Bundl([self, other])

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f"Предмет: {self.name} (вес: {self.weight}, цена: {self.prise})"

class Inventory:
    def __init__(self):
        self.items =[]

    def __add__(self, other):
        new_inventory = Inventory()
        new_inventory.items = self.items + [other]
        return new_inventory

    def __str__(self):
        if not self.items:
            return "Инвентарь пуст"

        items_str = "\n  ".join(str(item) for item in self.items)
        return f"Инвентарь:\n  {items_str}"



sword = Item("Меч", 5, 100)
shield = Item("Щит", 3, 50)

bundle = sword + shield
print(bundle)

inventory = Inventory()
print(inventory)

inventory = inventory + sword
print(inventory)

inventory = inventory + shield
print(inventory)


bow = Item("Лук", 2, 75)
print(bow < sword)
print(sword < bow)


sword2 = Item("Меч", 10, 200)
print(sword == sword2)
print(sword == shield)



