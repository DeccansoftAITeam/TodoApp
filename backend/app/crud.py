from sqlalchemy.orm import Session
from app import models, schemas

def get_todos(db: Session):
    return db.query(models.Todo).order_by(models.Todo.created_at.desc()).all()

def get_todo_by_id(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(
        title=todo.title,
        description=todo.description
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo: schemas.TodoUpdate):
    db_todo = get_todo_by_id(db, todo_id)
    if db_todo:
        if todo.title is not None:
            db_todo.title = todo.title
        if todo.description is not None:
            db_todo.description = todo.description
        if todo.is_completed is not None:
            db_todo.is_completed = todo.is_completed
        db.commit()
        db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = get_todo_by_id(db, todo_id)
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo
