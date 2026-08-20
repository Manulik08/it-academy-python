print("Задание 4")

import csv
with open("product.csv","w",encoding="utf-8") as file:
    file.write("name,price,category\n")
    file.write("Laptop,1200,Electronics\n")
    file.write("Phone,800,Electronics\n")
    file.write("Book,25,Books\n")
    file.write("Table,300,Furniture\n")

products = []
with open("product.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for i in reader:
        i['price'] = int(i["price"])
        products.append(i)

print("Название всех товаров:")
for i in products:
    print(i['name'])

goods = []
expensive_price = products[0]
print("Товары дороже 500:")
for i in products:
    if i['price']>500:
        goods.append(i)
        print(i['name'])

    if i['price']>expensive_price['price']:
        expensive_price = i

print(f"Количество товаров дороже 500: {len(goods)}")
print(f"Самый дорогой товар: {expensive_price['name']}({expensive_price['price']})")