print("Задание 3")
shop_list = ["хлеб", "молко"]
fake_copy = shop_list
true_copy = shop_list.copy()
fake_copy.append("сыр")
true_copy.remove("хлеб")
print(shop_list is fake_copy)
print(id(shop_list), id(fake_copy))
print(shop_list is true_copy)
print(id(shop_list), id(true_copy))
print(f"shop_list: {shop_list},\nfake_copy: {fake_copy},\ntrue_copy: {true_copy}")