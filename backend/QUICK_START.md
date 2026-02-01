# Quick Start Guide - Run Your Project Without PostgreSQL

## ✅ You DON'T need PostgreSQL!
The project is already configured to use SQLite, which works without any database installation.

## Steps to Run:

### 1. Install Python Packages
Open your terminal/command prompt and run:

```bash
cd C:\Users\VANSHITA SHAH\MatchMyTone\backend
python -m pip install -r requirements.txt
```

### 2. Run the Backend Server
```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

### 3. Run Your Frontend
In a NEW terminal window:
```bash
cd C:\Users\VANSHITA SHAH\MatchMyTone
npm start
# or
expo start
```

## That's it! 🎉

- **Database**: SQLite (automatically creates `matchmytone.db` file)
- **No PostgreSQL needed** for development
- **Backend runs on**: http://localhost:5000
- **Frontend connects automatically**

## Troubleshooting

### If you see "Python was not found":
- Make sure Python is installed
- Try using `py` instead of `python`: `py -m pip install -r requirements.txt`

### If you see "Module not found":
- Make sure you're in the `backend` folder
- Run: `python -m pip install -r requirements.txt`

### If backend doesn't start:
- Check if port 5000 is already in use
- The app will automatically create the database file when it starts





















