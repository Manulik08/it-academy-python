import copy


class Warrior:
    def __init__(self):
        self._health = 30
        self.attack = 5

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(0, value)

    @property
    def is_alive(self):
        return self._health > 0

    def take_damage(self, damage):
        self._health -= damage
        if self._health < 0:
            self._health = 0

    def attack_target(self, target):
        target.take_damage(self.attack)

    def __str__(self):
        return f"{self.__class__.__name__}, health: {self._health}, attack: {self.attack}"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            new_warrior = copy.deepcopy(self)
            new_warrior._health += other
            new_warrior.attack += other
            return new_warrior
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_warrior = copy.deepcopy(self)
            new_warrior._health *= other
            new_warrior.attack *= other
            return new_warrior
        return NotImplemented


class Fighter(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Mage(Warrior):
    def __init__(self):
        super().__init__()
        self.magic = 6

    def take_damage(self, damage):
        received_damage = damage - self.magic
        super().take_damage(received_damage)

    def attack_target(self, target):
        if target.attack < self.magic:
            damage_inflicted = self.attack + self.magic
        else:
            damage_inflicted = self.attack
        target.take_damage(damage_inflicted)


class Paladin(Warrior):
    def __init__(self):
        super().__init__()
        self._health = 50
        self.max_health = 50
        self.attack = 6

    def attack_target(self, target):
        old_hp = target._health
        super().attack_target(target)
        actual_damage = old_hp - target._health

        if actual_damage > 0:
            heal_amount = actual_damage * 0.2
            new_hp = self._health + heal_amount

            if new_hp > self.max_health:
                self._health = self.max_health
            else:
                self._health = new_hp


def fight(unit1, unit2):
    while unit1.is_alive and unit2.is_alive:
        unit1.attack_target(unit2)
        if not unit2.is_alive:
            break
        unit2.attack_target(unit1)
    return unit1.is_alive


class Army:
    def __init__(self):
        self.members = []

    def add_members(self, unit_class, count):
        for _ in range(count):
            self.members.append(unit_class())

    def __iter__(self):
        return iter(self.members)

    def __len__(self):
        return len(self.members)

    def __getitem__(self, item):
        if isinstance(item, slice):
            new_army = Army()
            new_army.members = self.members[item]
            return new_army
        return self.members[item]

    def __add__(self, other):
        if isinstance(other, (int, float)):
            new_army = Army()
            new_army.members = [unit + other for unit in self.members]
            return new_army
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_army = Army()
            new_army.members = [unit * other for unit in self.members]
            return new_army
        return NotImplemented

    @property
    def total_health(self):
        return sum(unit.health for unit in self.members)

    @property
    def total_attack(self):
        return sum(unit.attack for unit in self.members)

    @property
    def alive_members(self):
        return sum(1 for unit in self.members if unit.is_alive)



warrior = Warrior()
fighter = Fighter()
mage = Mage()
paladin = Paladin()

print(warrior)
print(fighter)
print(mage)
print(paladin)

print(f"Маг жив до боя? {mage.is_alive}")
print(f"Паладин жив до боя? {paladin.is_alive}")

result = fight(mage, paladin)

print(f"Победил первый юнит (Маг)? {result}")
print(f"Состояние Мага после боя: {mage}")
print(f"Состояние Паладина после боя: {paladin}")

fresh_fighter = Fighter()
print(f"Обычный боец: {fresh_fighter}")

super_fighter = fresh_fighter + 5
print(f"Прокачанный (+5): {super_fighter}")
print(f"Исходный боец не изменился: {fresh_fighter}")

mega_fighter = fresh_fighter * 2
print(f"Мега боец (*2): {mega_fighter}")

my_army = Army()

my_army.add_members(Fighter, 3)
my_army.add_members(Mage, 2)
my_army.add_members(Paladin, 1)

print(f"Всего воинов в армии: {len(my_army)}")
print(f"Общее здоровье армии: {my_army.total_health}")
print(f"Общая атака армии: {my_army.total_attack}")
print(f"Живых бойцов: {my_army.alive_members}")

print("Список всей армии:")
for unit in my_army:
    print(unit)

print(f"Первый воин в армии: {my_army[0]}")

sliced_army = my_army[1:3]
print("Вырезали кусочек армии (со 1-го по 3-й не включая):")
for unit in sliced_army:
    print(unit)

print(f"Здоровье армии до прокачки: {my_army.total_health}")

buffed_army = my_army + 10
print(f"Здоровье новой армии после прокачки (+10 каждому): {buffed_army.total_health}")
print(f"Старая армия осталась прежней: {my_army.total_health}")