# 📬 GmailBillTracker

A Python utility that connects to Gmail via the Gmail API to automatically extract and structure billing data — invoices, receipts, and payment confirmations — from your inbox.

---

## ✨ Features

- **Automated email processing** — scans 100+ emails via the Gmail API to identify and extract billing data
- **OAuth 2.0 authentication** — secure, token-based Gmail access following API security best practices
- **Keyword-based filtering** — targets relevant emails (invoices, receipts, confirmations) and reduces noise in results
- **Edge case handling** — manages forwarded threads, inconsistent formatting, and duplicate emails to improve reliability and output quality

---

## 🛠 Tech Stack

| Tool | Purpose |
| :--- | :--- |
| **Python** | Core application logic |
| **Gmail API** | Email access and filtering |
| **OAuth 2.0** | Secure authentication |

---

## ⚙️ Prerequisites

- Python 3.8+
- A Google account with Gmail
- A Google Cloud project with the Gmail API enabled and OAuth 2.0 credentials configured

---

## 🚀 Setup

**1. Clone the repository**
```bash
git clone https://github.com/Gogeta0011/GmailBillTracker.git
cd GmailBillTracker
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your credentials**

Download your `credentials.json` from the [Google Cloud Console](https://console.cloud.google.com/) and place it in the project root.

**4. Run**
```bash
python main.py
```

On first run, a browser window will open asking you to authorize Gmail access. A `token.json` file will be saved locally for future runs.

---

## 🔐 Security Notes

- `credentials.json` and `token.json` are excluded from version control via `.gitignore` — never commit these files.
- The app requests only the minimum required Gmail scopes (read-only).
- OAuth 2.0 ensures your Gmail password is never handled by the application.
