from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import sys
from pathlib import Path

# Ensure the project `backend` directory is on sys.path so `import app.*` works
_project_root = Path(__file__).resolve().parents[1]  # backend/
_root_str = str(_project_root)
if _root_str not in sys.path:
    sys.path.insert(0, _root_str)

from app.database import engine, Base #, ensure_database_exists
from app.routers import todos
from app import auth

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ensure database exists before creating tables
    #ensure_database_exists()
    # Create database tables on startup
    Base.metadata.create_all(bind=engine)
    yield

# Initialize FastAPI app
app = FastAPI(title="Todo API", lifespan=lifespan)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "https://dstodoapp-ezbre0c5cmaba0eg.canadacentral-01.azurewebsites.net",
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(todos.router, prefix="/api/todos", tags=["todos"])
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Todo API is running"}
