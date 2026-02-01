# 🔴 FIX: "Network request failed" - Backend Connection

## ✅ Good News!
Your app is **working perfectly**! The modules are loading fine. The only issue is connecting to the backend.

## The Problem
Windows Firewall is **blocking port 5000**, so your phone can't reach the backend server.

## 🚀 QUICK FIX (2 Minutes)

### Step 1: Open Windows Firewall
1. Press `Win + R`
2. Type `wf.msc` and press Enter

### Step 2: Allow Python Through Firewall
1. Click **"Allow an app or feature through Windows Defender Firewall"**
2. Click **"Change settings"** (top right, if needed)
3. Scroll down and find **"Python"** in the list
4. Check **BOTH** boxes:
   - ✅ **Private** (for your home network)
   - ✅ **Public** (for other networks)
5. Click **OK**

### Step 3: Test Again
1. Go back to your Expo Go app
2. Try logging in again
3. It should work now! ✅

---

## Alternative: Create Port Rule

If Python isn't in the list:

1. In Firewall, click **"Advanced settings"**
2. Click **"Inbound Rules"** → **"New Rule"**
3. Select **"Port"** → Click **Next**
4. Select **"TCP"**
5. Enter **"5000"** in "Specific local ports"
6. Click **Next**
7. Select **"Allow the connection"**
8. Click **Next**
9. Check **ALL** boxes (Domain, Private, Public)
10. Click **Next**
11. Name it: **"Flask Backend Port 5000"**
12. Click **Finish**

---

## ✅ Verify It's Working

After fixing firewall:
1. **Restart your backend** (Ctrl+C, then `python app.py`)
2. **Try login again** in Expo Go
3. You should see requests in your backend terminal!

---

## 🎯 Your Current Setup

- ✅ Backend running: `http://192.168.31.111:5000`
- ✅ App trying to connect: `http://192.168.31.111:5000/api`
- ✅ Both are correct!
- ❌ Firewall is blocking the connection

**Fix the firewall and it will work!** 🚀



