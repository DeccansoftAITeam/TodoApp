from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.database import engine, Base, ensure_database_exists
from app.routers import todos

@asynccontextmanager
async def lifespan(app: FastAPI):
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
    return {"message": "Todo API is running"}
