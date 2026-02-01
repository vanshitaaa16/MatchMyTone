# 🔧 Fix Firewall - Step by Step

## The Problem
Your firewall shows: **"Inbound connections that do not match a rule are blocked"**
And **"Public Profile is Active"** - your phone is using the Public profile!

## ✅ Solution: Enable Rule for Public Profile

### Step 1: Go to Inbound Rules
1. In the left pane, click **"Inbound Rules"**
2. You'll see a list of rules

### Step 2: Find Your Rule
Look for one of these:
- **"Flask Backend Port 5000"**
- **"python.exe"**
- Or any rule with port 5000

### Step 3: Check the Rule
1. **Right-click** on the rule
2. Click **"Properties"**
3. Go to **"Advanced"** tab
4. Under **"Profiles"**, make sure **ALL** are checked:
   - ✅ **Domain**
   - ✅ **Private**  
   - ✅ **Public** ← This is the important one!
5. Click **OK**

### Step 4: Make Sure Rule is Enabled
1. Look at the rule in the list
2. Check the **"Enabled"** column
3. If it says "No", right-click → **"Enable Rule"**

### Step 5: Test Again
1. Go back to your phone browser
2. Try: `http://192.168.31.111:5000/api/health`
3. Should work now! ✅

---

## If Rule Doesn't Exist or Doesn't Work

### Create New Rule:

1. In **"Inbound Rules"**, click **"New Rule..."** (right side)

2. Select **"Port"** → Click **Next**

3. Select **"TCP"**
   - Select **"Specific local ports"**
   - Enter: **5000**
   - Click **Next**

4. Select **"Allow the connection"** → Click **Next**

5. **Check ALL boxes:**
   - ✅ Domain
   - ✅ Private
   - ✅ **Public** ← Very important!
   - Click **Next**

6. Name it: **"Flask Backend Port 5000"**
   - Click **Finish**

7. **Test from phone again!**

---

## Alternative: Quick Test (Temporarily Disable)

To test if firewall is the issue:

1. Click **"Windows Defender Firewall Properties"** (in the overview)
2. Go to **"Public Profile"** tab
3. Under **"Firewall state"**, select **"Off"**
4. Click **OK**
5. **Test from phone** - if it works, firewall was the issue!
6. **Turn it back ON** and fix the rule properly

---

## Still Not Working?

Use **ngrok** - it bypasses all firewall issues:
See `USE_NGROK.md` for instructions!



