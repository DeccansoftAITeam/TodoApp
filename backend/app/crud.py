"""
CRUD (Create, Read, Update, Delete) operations module for Todo items.

This module contains all database operations for managing todo items.
It provides functions to interact with the database through SQLAlchemy ORM,
abstracting the database logic from the API endpoints.

Functions:
    get_todos: Retrieve all todo items from the database.
    get_todo_by_id: Retrieve a specific todo item by its ID.
    create_todo: Create a new todo item in the database.
    update_todo: Update an existing todo item.
    delete_todo: Delete a todo item from the database.
"""

from sqlalchemy.orm import Session
from app import models, schemas

def get_todos(db: Session):
    """
    Retrieve all todo items from the database.

    Fetches all todo items ordered by creation date in descending order
    (newest first). This provides a consistent ordering for the todo list.

    Args:
        db (Session): SQLAlchemy database session for executing queries.

    Returns:
        list[models.Todo]: A list of all todo items in the database,
                           ordered by creation date (newest first).

    Examples:
        >>> from app.database import SessionLocal
        >>> db = SessionLocal()
        >>> todos = get_todos(db)
        >>> print(f"Found {len(todos)} todos")
        Found 5 todos
    """
    return db.query(models.Todo).order_by(models.Todo.created_at.desc()).all()

def get_todo_by_id(db: Session, todo_id: int):
    """
    Retrieve a specific todo item by its unique identifier.

    Searches the database for a todo item with the given ID and returns
    it if found, or None if no matching todo exists.

    Args:
        db (Session): SQLAlchemy database session for executing queries.
        todo_id (int): The unique identifier of the todo item to retrieve.

    Returns:
        models.Todo | None: The todo item if found, None otherwise.

    Examples:
        >>> db = SessionLocal()
        >>> todo = get_todo_by_id(db, 1)
        >>> if todo:
        >>>     print(f"Found: {todo.title}")
        >>> else:
        >>>     print("Todo not found")
    """
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def create_todo(db: Session, todo: schemas.TodoCreate):
    """
    Create a new todo item in the database.

    Takes a TodoCreate schema, creates a new Todo model instance,
    adds it to the database, commits the transaction, and returns
    the created todo with its generated ID.

    Args:
        db (Session): SQLAlchemy database session for executing queries.
        todo (schemas.TodoCreate): Pydantic schema containing the todo data
                                   to be created (title and description).

    Returns:
        models.Todo: The newly created todo item including auto-generated
                     fields (id, is_completed, created_at).

    Examples:
        >>> from app.schemas import TodoCreate
        >>> db = SessionLocal()
        >>> new_todo = TodoCreate(title="Buy milk", description="From the store")
        >>> created = create_todo(db, new_todo)
        >>> print(f"Created todo with ID: {created.id}")
        Created todo with ID: 1
    """
    db_todo = models.Todo(
        title=todo.title,
        description=todo.description
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo: schemas.TodoUpdate):
    """
    Update an existing todo item in the database.

    Performs a partial update of a todo item, only modifying the fields
    that are provided in the TodoUpdate schema. If a field is None, it
    won't be updated. Returns the updated todo or None if not found.

    Args:
        db (Session): SQLAlchemy database session for executing queries.
        todo_id (int): The unique identifier of the todo item to update.
        todo (schemas.TodoUpdate): Pydantic schema containing the fields
                                   to update. All fields are optional.

    Returns:
        models.Todo | None: The updated todo item if found and updated,
                            None if the todo with the given ID doesn't exist.

    Examples:
        >>> from app.schemas import TodoUpdate
        >>> db = SessionLocal()
        >>> update_data = TodoUpdate(is_completed=True)
        >>> updated = update_todo(db, 1, update_data)
        >>> if updated:
        >>>     print(f"Todo {updated.id} marked as completed")
    """
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
    """
    Delete a todo item from the database.

    Finds and removes a todo item with the given ID from the database.
    The operation is committed immediately. Returns the deleted todo
    or None if the todo wasn't found.

    Args:
        db (Session): SQLAlchemy database session for executing queries.
        todo_id (int): The unique identifier of the todo item to delete.

    Returns:
        models.Todo | None: The deleted todo item if found and deleted,
                            None if the todo with the given ID doesn't exist.

    Examples:
        >>> db = SessionLocal()
        >>> deleted = delete_todo(db, 1)
        >>> if deleted:
        >>>     print(f"Deleted todo: {deleted.title}")
        >>> else:
        >>>     print("Todo not found")

    Notes:
        - The deletion is permanent and cannot be undone
        - The deleted todo object is returned before being removed from the session
    """
    db_todo = get_todo_by_id(db, todo_id)
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo
