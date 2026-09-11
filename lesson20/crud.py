from sqlalchemy.orm import Session
from models import User, Task
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from database import SessionLocal

def create_user(db: Session, username: str, email: str):
    try:
        new_user = User(name=name, email=email)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        print(f"Пользователь {username} успешно добавлен")
        return new_user.id
    except IntegrityError:
        db.rollback()
        print("Пользователь с таким email уже существует")
        return None

def get_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id):
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, name: str, email: str):
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        print(f"Пользователь с ID {user_id} не найден!")
        return None
    try:
        if name:
            db_user.name = name
        if email:
            db_user.email = email
        db.commit()
        db.refresh(db_user)
        print(f"Пользователь {db_user.name} успешно обновлён")
        return db_user
    except IntegrityError:
        db.rollback()
        print(f"Имя или email уже заняты другим пользователем")
        return None

def delete_user(db: Session, user_id: int):
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        print(f"Пользователь с ID {user_id} не найден!")
        return False
    db.delete(db_user)
    db.commit()
    print(f"Пользователь {db_user.name} удалён")
    return True

def create_task(db: Session, user_id: int, title: str, description: str = ""):
    user = get_user_by_id(db, user_id)
    if not user:
        print(f"Пользователь с ID {user_id} не найден!")
        return None
    try:
        db_task = Task(
            title=title,
            description=description,
            user_id=user_id,
            status="new"
        )
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        print(f"Задача '{title}' успешно создана")
        return db_task
    except Exception as e:
        db.rollback()
        print(f"Ошибка при создании задачи: {e}")
        return None

def get_tasks(db: Session):
    return db.query(Task).all()

def get_tasks_by_user(db: Session, user_id: int):
    return db.query(Task).filter(Task.user_id == user_id).all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def update_task_status(db: Session, task_id: int, status: str):
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        print(f"Задача с ID {task_id} не найдена!")
        return None

    db_task.status = status
    db.commit()
    db.refresh(db_task)
    print(f"Статус задачи обновлён на '{status}'")
    return db_task


def delete_task(db: Session, task_id: int):
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        print(f"Задача с ID {task_id} не найдена!")
        return False

    db.delete(db_task)
    db.commit()
    print(f"Задача '{db_task.title}' удалена")
    return True


