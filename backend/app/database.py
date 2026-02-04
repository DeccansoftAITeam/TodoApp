"""
Database configuration and session management module.

This module handles all database-related configuration including connection
strings, engine creation, session management, and database initialization.
It uses SQLAlchemy for ORM functionality and connects to a SQL Server database.

Attributes:
    master_connection_string (str): Connection string for SQL Server master database.
    connection_string (str): Connection string for the TodoDB database.
    DATABASE_URL (str): SQLAlchemy database URL with ODBC driver.
    engine (Engine): SQLAlchemy engine instance for database operations.
    SessionLocal (sessionmaker): Factory for creating database sessions.
    Base (DeclarativeMeta): Base class for SQLAlchemy models.

Functions:
    ensure_database_exists: Creates the TodoDB database if it doesn't exist.
    get_db: Dependency function that provides database sessions to endpoints.
"""

from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
import pyodbc

# SQL Server connection string with Windows Authentication (master database)
master_connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=master;"
    "Trusted_Connection=yes;"
)

# SQL Server connection string for TodoDB
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=TodoDB;"
    "Trusted_Connection=yes;"
)

def ensure_database_exists():
    """
    Ensure that the TodoDB database exists, creating it if necessary.

    This function connects to the SQL Server master database and checks if
    the TodoDB database exists. If it doesn't exist, the function creates it.
    This is typically called during application startup.

    Raises:
        Exception: If there's an error connecting to SQL Server or creating
                   the database. The exception is caught and logged.

    Examples:
        >>> ensure_database_exists()
        Database 'TodoDB' already exists

        >>> # Or if database doesn't exist
        >>> ensure_database_exists()
        Database 'TodoDB' created successfully

    Notes:
        - Requires SQL Server to be running on localhost\\SQLEXPRESS
        - Uses Windows Authentication (Trusted_Connection)
        - Errors are printed but don't stop execution
    """
    try:
        # Connect to master database
        conn = pyodbc.connect(master_connection_string)
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Check if database exists
        cursor.execute("SELECT database_id FROM sys.databases WHERE Name = 'TodoDB'")
        if not cursor.fetchone():
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE TodoDB")
            print("Database 'TodoDB' created successfully")
        else:
            print("Database 'TodoDB' already exists")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error ensuring database exists: {e}")

# Create SQLAlchemy engine
DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={quote_plus(connection_string)}"
engine = create_engine(DATABASE_URL, echo=True)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class
Base = declarative_base()

def get_db():
    """
    Provide a database session to API endpoints.

    This function is a dependency that creates a new SQLAlchemy session
    for each request and ensures it's properly closed after the request
    is completed. It uses FastAPI's dependency injection system.

    Yields:
        Session: A SQLAlchemy database session instance.

    Examples:
        >>> from fastapi import Depends
        >>> @app.get("/todos")
        >>> def get_todos(db: Session = Depends(get_db)):
        >>>     return db.query(Todo).all()

    Notes:
        - The session is automatically committed if no exceptions occur
        - The session is always closed in the finally block
        - Should be used with FastAPI's Depends() for dependency injection
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
