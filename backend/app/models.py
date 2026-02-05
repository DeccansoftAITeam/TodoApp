"""
Database models module for the Todo API.

This module defines SQLAlchemy ORM models that represent database tables.
It contains the Todo model which maps to the 'todos' table in the database.

Classes:
    Todo: SQLAlchemy model representing a todo item in the database.
"""

from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Todo(Base):
    """
    SQLAlchemy model representing a todo item.

    This model defines the structure of the 'todos' table in the database,
    including all columns and their constraints. Each todo item has a unique
    identifier, title, optional description, completion status, and timestamp.

    Attributes:
        id (int): Primary key identifier for the todo item.
        title (str): Title of the todo item (max 200 characters, required).
        description (str): Optional detailed description of the todo item.
        is_completed (bool): Completion status of the todo (default: False).
        created_at (datetime): Timestamp when the todo was created (auto-generated).

    Table:
        todos: Database table name where todo items are stored.

    Examples:
        >>> from sqlalchemy.orm import Session
        >>> todo = Todo(title="Buy groceries", description="Milk, eggs, bread")
        >>> session.add(todo)
        >>> session.commit()
    """
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    is_completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
