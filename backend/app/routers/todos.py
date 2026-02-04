"""
API router module for Todo endpoints.

This module defines all REST API endpoints for managing todo items.
It implements standard CRUD operations (Create, Read, Update, Delete)
using FastAPI's routing system and depends on the CRUD operations
defined in the crud module.

Attributes:
    router (APIRouter): FastAPI router instance for todo-related endpoints.

Endpoints:
    GET /: Retrieve all todo items.
    GET /{todo_id}: Retrieve a specific todo item by ID.
    POST /: Create a new todo item.
    PUT /{todo_id}: Update an existing todo item.
    DELETE /{todo_id}: Delete a todo item.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.TodoResponse])
def read_todos(db: Session = Depends(get_db)):
    """
    Retrieve all todo items.

    Fetches and returns a list of all todo items from the database,
    ordered by creation date (newest first).

    Args:
        db (Session): Database session injected by FastAPI's dependency system.

    Returns:
        list[schemas.TodoResponse]: List of all todo items with their details.

    Examples:
        >>> # GET /api/todos/
        >>> # Response: [
        >>> #   {"id": 1, "title": "Task 1", "description": "...", ...},
        >>> #   {"id": 2, "title": "Task 2", "description": "...", ...}
        >>> # ]
    """
    todos = crud.get_todos(db)
    return todos

@router.get("/{todo_id}", response_model=schemas.TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific todo item by its ID.

    Fetches a single todo item from the database using its unique identifier.
    Returns a 404 error if the todo item is not found.

    Args:
        todo_id (int): The unique identifier of the todo item to retrieve.
        db (Session): Database session injected by FastAPI's dependency system.

    Returns:
        schemas.TodoResponse: The requested todo item with all its details.

    Raises:
        HTTPException: 404 error if the todo item with the given ID doesn't exist.

    Examples:
        >>> # GET /api/todos/1
        >>> # Response: {"id": 1, "title": "Buy milk", "is_completed": false, ...}
        >>> 
        >>> # GET /api/todos/999 (non-existent)
        >>> # Response: 404 {"detail": "Todo not found"}
    """
    todo = crud.get_todo_by_id(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/", response_model=schemas.TodoResponse, status_code=201)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    """
    Create a new todo item.

    Accepts todo data in the request body and creates a new todo item
    in the database. Returns the created todo with its generated ID
    and default values.

    Args:
        todo (schemas.TodoCreate): The todo data to create (title and description).
        db (Session): Database session injected by FastAPI's dependency system.

    Returns:
        schemas.TodoResponse: The newly created todo item with all fields.

    Examples:
        >>> # POST /api/todos/
        >>> # Request body: {"title": "New task", "description": "Task details"}
        >>> # Response: {
        >>> #   "id": 3,
        >>> #   "title": "New task",
        >>> #   "description": "Task details",
        >>> #   "is_completed": false,
        >>> #   "created_at": "2026-02-04T07:49:05.197Z"
        >>> # }
    """
    return crud.create_todo(db, todo)

@router.put("/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    """
    Update an existing todo item.

    Performs a partial update of a todo item. Only the fields provided
    in the request body will be updated. Returns a 404 error if the
    todo item is not found.

    Args:
        todo_id (int): The unique identifier of the todo item to update.
        todo (schemas.TodoUpdate): The fields to update (all optional).
        db (Session): Database session injected by FastAPI's dependency system.

    Returns:
        schemas.TodoResponse: The updated todo item with all its details.

    Raises:
        HTTPException: 404 error if the todo item with the given ID doesn't exist.

    Examples:
        >>> # PUT /api/todos/1
        >>> # Request body: {"is_completed": true}
        >>> # Response: {"id": 1, "title": "...", "is_completed": true, ...}
        >>> 
        >>> # PUT /api/todos/999 (non-existent)
        >>> # Response: 404 {"detail": "Todo not found"}
    """
    db_todo = crud.update_todo(db, todo_id, todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@router.delete("/{todo_id}", response_model=schemas.TodoResponse)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """
    Delete a todo item.

    Removes a todo item from the database permanently. Returns the deleted
    todo item data. Returns a 404 error if the todo item is not found.

    Args:
        todo_id (int): The unique identifier of the todo item to delete.
        db (Session): Database session injected by FastAPI's dependency system.

    Returns:
        schemas.TodoResponse: The deleted todo item with all its details.

    Raises:
        HTTPException: 404 error if the todo item with the given ID doesn't exist.

    Examples:
        >>> # DELETE /api/todos/1
        >>> # Response: {"id": 1, "title": "...", ...}
        >>> 
        >>> # DELETE /api/todos/999 (non-existent)
        >>> # Response: 404 {"detail": "Todo not found"}

    Notes:
        - The deletion is permanent and cannot be undone
        - The deleted todo data is returned in the response
    """
    db_todo = crud.delete_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo
