from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app import models, schemas
from app.auth import create_access_token, verify_token
from datetime import datetime
import os

Base.metadata.create_all(bind=engine)

app = FastAPI(title="GmailBillTracker 2.0")
security = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/auth/login")
def login(username: str, password: str):
    # Simple demo login — replace with real user check later
    if username == "demo" and password == "demo":
        token = create_access_token({"sub": username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/receipts", response_model=schemas.ReceiptOut)
def create_receipt(
    receipt: schemas.ReceiptCreate,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    verify_token(credentials.credentials)
    db_receipt = models.Receipt(
        vendor=receipt.vendor,
        amount=receipt.amount,
        date=receipt.date,
        category=receipt.category,
    )
    db.add(db_receipt)
    db.commit()
    db.refresh(db_receipt)
    return db_receipt

@app.get("/receipts", response_model=list[schemas.ReceiptOut])
def list_receipts(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    verify_token(credentials.credentials)
    return db.query(models.Receipt).all()

@app.get("/")
def root():
    return {"message": "GmailBillTracker 2.0 is running"}
