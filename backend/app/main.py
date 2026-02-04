"""
Main application module for the Todo API.

This module initializes the FastAPI application, configures middleware,
sets up database connections, and includes all API routers. It serves as
the entry point for the Todo API backend service.

Attributes:
    app (FastAPI): The main FastAPI application instance.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.database import engine, Base, ensure_database_exists
from app.routers import todos

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manage the lifespan of the FastAPI application.

    This async context manager handles startup and shutdown events for the application.
    On startup, it ensures the database exists and creates all necessary tables.

    Args:
        app (FastAPI): The FastAPI application instance.

    Yields:
        None: Control is yielded to the application during its runtime.

    Examples:
        This function is automatically called by FastAPI and should not be
        invoked directly. It's registered with the FastAPI app during initialization.
    """
    # Ensure database exists before creating tables
    ensure_database_exists()
    # Create database tables on startup
    Base.metadata.create_all(bind=engine)
    yield

# Initialize FastAPI app
app = FastAPI(title="Todo API", lifespan=lifespan)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(todos.router, prefix="/api/todos", tags=["todos"])

@app.get("/")
def read_root():
    """
    Health check endpoint for the API.

    Returns a simple message to indicate that the API is running and accessible.
    This endpoint can be used for health checks and monitoring.

    Returns:
        dict: A dictionary containing a status message.
            - message (str): Confirmation message that the API is operational.

    Examples:
        >>> response = read_root()
        >>> print(response)
        {'message': 'Todo API is running'}
    """
    return {"message": "Todo API is running"}
