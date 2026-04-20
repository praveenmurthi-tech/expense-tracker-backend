from datetime import date, datetime
from typing import Optional

from sqlmodel import SQLModel


# ----------------------------
# CREATE EXPENSE SCHEMA
# ----------------------------
class ExpenseCreate(SQLModel):
    amount: float
    category: str
    description: Optional[str] = None
    date: date

    # required for retry safety (VERY IMPORTANT)
    idempotency_key: str


# ----------------------------
# READ EXPENSE SCHEMA
# ----------------------------
class ExpenseRead(SQLModel):
    id: int
    amount: float
    category: str
    description: Optional[str]
    date: date
    created_at: datetime
    idempotency_key: str

    class Config:
        from_attributes = True