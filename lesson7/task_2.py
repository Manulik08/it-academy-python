print("Задание 2")

users = [15, 42, 18, 90, 11, 42, 35, 18]
users_set = set()
user_twin = None
for user in users:
    if user in users_set:
        user_twin = user
    users_set.add(user)
    if user == user_twin:
        print(f"Первый повтор: {user_twin}")
        break
else:
    print("Повторов нет")
