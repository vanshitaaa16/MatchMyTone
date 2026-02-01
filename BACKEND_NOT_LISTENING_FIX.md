# 🔴 Backend Not Listening on Port 5000

## The Problem
The backend shows it's "running" but `netstat` shows it's **NOT listening on port 5000**.

This means the Flask server isn't actually accepting connections.

## ✅ FIX: Restart Backend Properly

### Step 1: Stop Current Backend
1. Go to your backend terminal
2. Press `Ctrl+C` to stop it
3. Wait for it to fully stop

### Step 2: Check for Port Conflicts
```bash
netstat -ano | findstr :5000
```

If you see anything, another process is using port 5000!

### Step 3: Restart Backend
```bash
cd backend
python app.py
```

### Step 4: Verify It's Listening
In a NEW terminal, run:
```bash
netstat -ano | findstr :5000
```

You should see:
```
TCP    0.0.0.0:5000    0.0.0.0:0    LISTENING    [PID]
```

### Step 5: Test from Computer
Open browser on your computer:
```
http://localhost:5000/api/health
```

Should show: `{"status": "ok", "message": "API is running"}`

### Step 6: Test from Phone
Open browser on your phone:
```
http://192.168.31.111:5000/api/health
```

Should work now! ✅

---

## If Port 5000 is Already in Use

**Find what's using it:**
```bash
netstat -ano | findstr :5000
```

**Kill the process:**
```bash
taskkill /PID [PID_NUMBER] /F
```

**Then restart backend**

---

## Alternative: Use Different Port

If port 5000 is blocked, use port 5001:

1. **Update `backend/app.py`:**
   ```python
   app.run(debug=True, host='0.0.0.0', port=5001)
   ```

2. **Update `src/api.js`:**
   ```javascript
   return 'http://192.168.31.111:5001/api';
   ```

3. **Restart both backend and app**



