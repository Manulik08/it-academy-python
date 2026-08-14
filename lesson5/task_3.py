from copy import deepcopy
hero = {
 "name": "Воин",
 "level": 1,
 "inventory": [
 "меч",
 "щит"
 ],
 "skills": {
 "attack": 10,
 "defense": 5
 }
}

hero_2 = deepcopy(hero)
hero_3 = deepcopy(hero)
hero["name"] = "Bob"
hero_2["inventory"].append("лук")
hero_3["skills"]["attack"] += 10
print(hero)
print(hero_2)
print(hero_3)

# выбрана функция deepcopy т.к. копирование вложенных объектов у нее глубже
