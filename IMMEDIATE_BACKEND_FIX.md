# 🚨 IMMEDIATE FIX: Backend Not Listening

## The Problem
Your backend terminal shows it's "running", but it's **NOT actually listening on port 5000**.

Python is running, but Flask isn't bound to the port.

## ✅ FIX NOW (Do This):

### Step 1: Stop Backend
1. Go to your **backend terminal** (where Flask is running)
2. Press **`Ctrl+C`** to stop it
3. Wait until it says "Stopped" or you get a new prompt

### Step 2: Kill Any Stuck Python Processes
Open a NEW terminal and run:
```bash
taskkill /F /IM python.exe
```

### Step 3: Restart Backend
```bash
cd backend
python app.py
```

### Step 4: Look for This Output
You should see:
```
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5000
* Running on http://192.168.31.111:5000
```

**If you see errors instead**, share them with me!

### Step 5: Verify It's Listening
In a NEW terminal, run:
```bash
netstat -ano | findstr :5000
```

You should see:
```
TCP    0.0.0.0:5000    0.0.0.0:0    LISTENING
```

### Step 6: Test Again
1. **On your computer browser:** `http://localhost:5000/api/health`
2. **On your phone browser:** `http://192.168.31.111:5000/api/health`

Both should work now! ✅

---

## Common Issues

### Issue: "Address already in use"
**Fix:** Port 5000 is taken by another process
```bash
# Find what's using it:
netstat -ano | findstr :5000
# Kill it:
taskkill /PID [PID_NUMBER] /F
```

### Issue: Database connection error
**Fix:** Make sure PostgreSQL is running
```bash
# Start PostgreSQL service
```

### Issue: Import errors
**Fix:** Install dependencies
```bash
cd backend
pip install -r requirements.txt
```

---

## After Restarting

**Share with me:**
1. What output do you see when starting backend?
2. Does `netstat` show port 5000 listening?
3. Can you access `http://localhost:5000/api/health` from computer?



