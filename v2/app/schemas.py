from pydantic import BaseModel
from datetime import date

class ReceiptCreate(BaseModel):
    vendor: str
    amount: float
    date: date
    category: str | None = None

class ReceiptOut(ReceiptCreate):
    id: int

    class Config:
        from_attributes = True
