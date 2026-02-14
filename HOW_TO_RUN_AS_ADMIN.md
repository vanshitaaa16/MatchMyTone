# How to Run FIX_FIREWALL_NOW.bat as Administrator

## Method 1: From Windows File Explorer (Easiest)

1. **Close VS Code or minimize it**

2. **Open Windows File Explorer:**
   - Press `Win + E` (Windows key + E)
   - OR click the folder icon in your taskbar

3. **Navigate to your project:**
   - Go to: `C:\Users\VANSHITA SHAH\MatchMyTone`
   - OR in VS Code, right-click `FIX_FIREWALL_NOW.bat` → **"Reveal in File Explorer"**

4. **Right-click on `FIX_FIREWALL_NOW.bat`**

5. **Select "Run as administrator"** from the menu
   - You'll see a shield icon next to this option

6. **Click "Yes"** when Windows asks for permission

7. **A black command window will open** - let it run and it will create the firewall rule

## Method 2: From VS Code (Using Terminal)

1. **In VS Code, open the terminal:**
   - Press `` Ctrl + ` `` (backtick key, usually above Tab)
   - OR go to Terminal → New Terminal

2. **Run this command:**
   ```powershell
   Start-Process -FilePath ".\FIX_FIREWALL_NOW.bat" -Verb RunAs
   ```

3. **Click "Yes"** when Windows asks for permission

## Method 3: From Command Prompt (Manual)

1. **Open Command Prompt as Administrator:**
   - Press `Win + X`
   - Select "Windows PowerShell (Admin)" or "Terminal (Admin)"
   - Click "Yes" when asked for permission

2. **Navigate to your project:**
   ```bash
   cd "C:\Users\VANSHITA SHAH\MatchMyTone"
   ```

3. **Run the script:**
   ```bash
   .\FIX_FIREWALL_NOW.bat
   ```

## What You Should See

After running as administrator, you should see:
```
========================================
  Fix Windows Firewall for Backend
========================================

Creating firewall rule...
SUCCESS: Firewall rule created!
```

## If You Get an Error

**"Access Denied" or "Permission Denied":**
- Make sure you selected "Run as administrator"
- Try Method 1 (File Explorer) - it's the most reliable

**"Rule already exists":**
- That's OK! The rule is already there, which means it might already be configured
- Try restarting your backend and testing again

## After Running the Script

1. **Restart your backend** (stop with Ctrl+C, then start again)
2. **Test in browser:** `http://192.168.31.111:5000/api/health`
3. **Reload your app** (press `Shift + R` in Expo terminal)
4. **Try login again**




