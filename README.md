# Excel Mock Interviewer

A web application that conducts mock Excel interviews using voice input and Google Gemini AI for real-time evaluation.

---

## Features
- Voice-based Excel questions
- Real-time evaluation using Gemini AI
- Progress tracking with a progress bar
- Scrollable results display
- Modern, responsive UI

---

## Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/<YOUR_USERNAME>/excel-mock-interviewer.git
cd excel-mock-interviewer
Install dependencies

pip install -r requirements.txt


Set your Google API Key

export GOOGLE_API_KEY="YOUR_API_KEY"  # Linux / Mac
set GOOGLE_API_KEY="YOUR_API_KEY"     # Windows


Run the Flask app

python app.py


Open in browser:
Go to http://127.0.0.1:5000

Folder Structure
excel-mock-interviewer/
│
├── templates/
│   └── index.html          # Frontend HTML
├── static/                 # Optional: CSS/JS
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
└── README.md               # Project description

Future Improvements

Add scoring system

Save past interviews for user progress tracking

Dark/light mode toggle

Hints or example answers for wrong responses

Export results as PDF/CSV


---

## **4️⃣ Optional Enhancements**
- Add **screenshots** of your app:
```markdown
![Screenshot](screenshots/interview.png)


Add badges for Python version, license, or GitHub stars:

![Python](https://img.shields.io/badge/python-3.11-blue)