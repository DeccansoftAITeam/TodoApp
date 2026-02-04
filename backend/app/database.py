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

# Function to ensure database exists
def ensure_database_exists():
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

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
