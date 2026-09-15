from database import SessionLocal, engine, Base
from models import User, Task
import crud

Base.metadata.create_all(bind=engine)

def menu():
    print("Система управления задачами:")
    print("1. Создать пользователя")
    print("2. Показать всех пользователей")
    print("3. Создать задачу")
    print("4. Показать все задачи")
    print("5. Показать мои задачи")
    print("6. Изменить статус задачи")
    print("7. Удалить задачу")
    print("8. Найти задачу по ID")
    print("9. Обновить пользователя")
    print("10. Удалить пользователя")
    print("0. Выход")

def create_user_menu():
    print("Создание пользователя")
    name = input("Введите имя пользователя: ").strip()
    email = input("Введите email: ").strip()

    if not name or not email:
        print("Имя и email обязательны")
        return
    with SessionLocal() as session:
        user_id = crud.create_user(session, name, email)
        if user_id:
            print(f"Пользователь создан с ID: {user_id}")
        else:
            print("Не удалось создать пользователя")


def show_users_menu():
    with SessionLocal() as session:
        users = crud.get_users(session)
        if not users:
            print("Пользователей нет")
            return

        print("Список пользователей")
        for user in users:
            print(f"ID: {user.id}, Имя: {user.name}, Email: {user.email}")


def create_task_menu():
    print("Создание задачи")

    with SessionLocal() as session:
        users = crud.get_users(session)
        if not users:
            print("Сначала создайте пользователя")
            return

        print("Доступные пользователи:")
        for user in users:
            print(f"{user.id}. {user.name}")

        try:
            user_id = int(input("Выберите ID пользователя: "))
        except ValueError:
            print("Неверный ID")
            return

        title = input("Введите название задачи: ").strip()
        description = input("Введите описание (необязательно): ").strip()

        if not title:
            print("Название задачи обязательно")
            return
        task = crud.create_task(session, user_id, title, description)
        if task:
            print(f"Задача создана с ID: {task.id}")
        else:
            print("Не удалось создать задачу")


def show_tasks_menu():
    with SessionLocal() as session:
        tasks = crud.get_tasks(session)
        if not tasks:
            print("Задач нет")
            return

        print("Все задачи:")
        for task in tasks:
            user = task.user
            print(f"ID: {task.id} - [{task.status}] - {task.title}")
            print(f"Пользователь: {user.name}\nОписание: {task.description or '-'}")


def show_my_tasks_menu():
    with SessionLocal() as session:
        users = crud.get_users(session)
        if not users:
            print("Пользователей нет")
            return

        print("Выберите пользователя:")
        for user in users:
            print(f"  {user.id}. {user.name}")

        try:
            user_id = int(input("\nВведите ID пользователя: "))
        except ValueError:
            print("Неверный ID!")
            return

        user = crud.get_user_by_id(session, user_id)
        if not user:
            print(f"Пользователь с ID {user_id} не найден")
            return

        tasks = crud.get_tasks_by_user(session, user_id)

        if not tasks:
            print(f" У пользователя {user.name} нет задач")
            return

        print(f"Задачи пользователя {user.name}")
        for task in tasks:
            print(f"ID: {task.id} - [{task.status}] - {task.title}")
            print(f"   Описание: {task.description or '-'}")


def update_task_status_menu():
    with SessionLocal() as session:
        try:
            task_id = int(input("Введите ID задачи: "))
        except ValueError:
            print("Неверный ID")
            return

        task = crud.get_task_by_id(session, task_id)
        if not task:
            print("Задача не найдена!")
            return

        print(f"Текущий статус: {task.status}")
        print("Доступные статусы: new, in_progress, done")
        new_status = input("Введите новый статус: ").strip()

        if new_status not in ["new", "in_progress", "done"]:
            print("Неверный статус")
            return

        updated_task = crud.update_task_status(session, task_id, new_status)
        if updated_task:
            print(f"Статус обновлён на '{updated_task.status}'")


def delete_task_menu():
    with SessionLocal() as session:
        try:
            task_id = int(input("Введите ID задачи для удаления: "))
        except ValueError:
            print("Неверный ID")
            return

        if crud.delete_task(session, task_id):
            print("Задача удалена")
        else:
            print("Задача не найдена")


def update_user_menu():
    with SessionLocal() as session:
        try:
            user_id = int(input("Введите ID пользователя для обновления: "))
        except ValueError:
            print("Неверный ID")
            return

        user = crud.get_user_by_id(session, user_id)
        if not user:
            print(f"Пользователь с ID {user_id} не найден")
            return

        print(f"Текущие данные: {user.name} | {user.email}")
        new_name = input("Новое имя (оставьте пустым, чтобы не менять): ").strip()
        new_email = input("Новый email (оставьте пустым, чтобы не менять): ").strip()

        if not new_name and not new_email:
            print("Ничего не изменено")
            return

        updated_user = crud.update_user(session, user_id, new_name or None, new_email or None)
        if updated_user:
            print(f"Данные обновлены: {updated_user.name} - {updated_user.email}")


def delete_user_menu():
    with SessionLocal() as session:
        try:
            user_id = int(input("Введите ID пользователя для удаления: "))
        except ValueError:
            print("Неверный ID!")
            return

        user = crud.get_user_by_id(session, user_id)
        if not user:
            print(f"Пользователь с ID {user_id} не найден")
            return

        confirm = input(f"Удалить пользователя '{user.name}' и все его задачи? (да/нет): ")
        if confirm.lower() != "да":
            print("Удаление отменено")
            return

        if crud.delete_user(session, user_id):
            print("Пользователь удалён")
        else:
            print("Пользователь не найден")


def find_task_menu():
    with SessionLocal() as session:
        try:
            task_id = int(input("Введите ID задачи: "))
        except ValueError:
            print("Неверный ID!")
            return

        task = crud.get_task_by_id(session, task_id)
        if not task:
            print(f"Задача с ID {task_id} не найдена!")
            return

        print(f"Задача ID={task.id}")
        print(f"Название: {task.title}")
        print(f"Описание: {task.description or '-'}")
        print(f"Статус: {task.status}")
        print(f"Пользователь: {task.owner.name}")


def main():
    print("Добро пожаловать в Task Manager!")

    while True:
        menu()
        choice = input("Выберите действие (0-10): ").strip()

        if choice == "1":
            create_user_menu()
        elif choice == "2":
            show_users_menu()
        elif choice == "3":
            create_task_menu()
        elif choice == "4":
            show_tasks_menu()
        elif choice == "5":
            show_my_tasks_menu()
        elif choice == "6":
            update_task_status_menu()
        elif choice == "7":
            delete_task_menu()
        elif choice == "8":
            find_task_menu()
        elif choice == "9":
            update_user_menu()
        elif choice == "10":
            delete_user_menu()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
