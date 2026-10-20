from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "GmailBillTracker 2.0 is running"

def test_login_and_create_receipt():
    login = client.post("/auth/login", params={"username": "demo", "password": "demo"})
    assert login.status_code == 200
    token = login.json()["access_token"]

    receipt = {
        "vendor": "Test Store",
        "amount": 12.50,
        "date": "2026-10-20",
        "category": "groceries",
    }
    response = client.post(
        "/receipts",
        json=receipt,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.json()["vendor"] == "Test Store"
