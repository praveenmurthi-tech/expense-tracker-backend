from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import expenses
from app.db.session import engine
from app.db.base import init_db

app = FastAPI(title="Expense Tracker API")

# =========================
# CORS CONFIGURATION
# =========================
oallowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins if allowed_origins != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# STARTUP EVENT
# =========================
@app.on_event("startup")
def on_startup():
    init_db(engine)

# =========================
# ROUTES
# =========================
app.include_router(expenses.router, prefix="/api/v1")


# =========================
# HEALTH CHECK (IMPORTANT FOR RENDER)
# =========================
@app.get("/")
def health_check():
    return {"status": "Backend is running 🚀"}