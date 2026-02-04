"""
Pydantic schemas module for the Todo API.

This module defines Pydantic models used for request validation and response
serialization. These schemas ensure data integrity and provide automatic
validation for API endpoints.

Classes:
    TodoBase: Base schema with common todo attributes.
    TodoCreate: Schema for creating a new todo item.
    TodoUpdate: Schema for updating an existing todo item.
    TodoResponse: Schema for todo item API responses.
"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TodoBase(BaseModel):
    """
    Base Pydantic model for todo items with common attributes.

    This model serves as the foundation for other todo-related schemas,
    containing the core attributes that are shared across different operations.

    Attributes:
        title (str): The title of the todo item (required).
        description (Optional[str]): Optional detailed description of the todo.

    Examples:
        >>> todo_data = TodoBase(title="Complete project", description="Finish by Friday")
        >>> print(todo_data.title)
        'Complete project'
    """
    title: str
    description: Optional[str] = None

class TodoCreate(TodoBase):
    """
    Schema for creating a new todo item.

    Inherits all attributes from TodoBase and is used to validate
    incoming requests when creating new todo items via the API.

    Inherits:
        TodoBase: Base schema with title and description attributes.

    Examples:
        >>> new_todo = TodoCreate(title="Write documentation")
        >>> # This schema is typically used automatically by FastAPI
    """
    pass

class TodoUpdate(BaseModel):
    """
    Schema for updating an existing todo item.

    All fields are optional to allow partial updates. Only the fields
    provided in the request will be updated in the database.

    Attributes:
        title (Optional[str]): Updated title for the todo item.
        description (Optional[str]): Updated description for the todo item.
        is_completed (Optional[bool]): Updated completion status.

    Examples:
        >>> update_data = TodoUpdate(is_completed=True)
        >>> # Only the completion status will be updated
    """
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

class TodoResponse(TodoBase):
    """
    Schema for todo item API responses.

    This schema is used to serialize todo items when returning them
    from API endpoints. It includes all attributes from the database model.

    Attributes:
        id (int): Unique identifier of the todo item.
        is_completed (bool): Current completion status of the todo.
        created_at (datetime): Timestamp when the todo was created.

    Config:
        from_attributes (bool): Enables ORM mode for SQLAlchemy model compatibility.

    Examples:
        >>> # This schema is automatically used by FastAPI for response serialization
        >>> # response = TodoResponse.from_orm(db_todo)
    """
    id: int
    is_completed: bool
    created_at: datetime

    class Config:
        from_attributes = True
