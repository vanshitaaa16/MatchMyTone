# PostgreSQL Setup Guide for Windows

## Step 1: Install PostgreSQL

1. **Download PostgreSQL:**
   - Go to: https://www.postgresql.org/download/windows/
   - Click "Download the installer"
   - Download PostgreSQL 15 or 16 (latest version)

2. **Install PostgreSQL:**
   - Run the installer
   - **Important:** Remember the password you set for the `postgres` user (default username)
   - Default port: `5432` (keep this)
   - Complete the installation

## Step 2: Create the Database

### Option A: Using pgAdmin (GUI - Recommended for beginners)

1. **Open pgAdmin:**
   - Search for "pgAdmin 4" in Windows Start menu
   - Open it

2. **Connect to Server:**
   - Enter the password you set during installation
   - You'll see "PostgreSQL 15" (or your version) in the left panel

3. **Create Database:**
   - Right-click on "Databases" → "Create" → "Database..."
   - Name: `matchmytone`
   - Click "Save"

### Option B: Using Command Line (psql)

1. **Open Command Prompt or PowerShell**

2. **Connect to PostgreSQL:**
   ```bash
   psql -U postgres
   ```
   - Enter your password when prompted

3. **Create the database:**
   ```sql
   CREATE DATABASE matchmytone;
   ```

4. **Exit psql:**
   ```sql
   \q
   ```

## Step 3: Update Database Connection (if needed)

If your PostgreSQL username/password is different from `postgres:postgres`, create a `.env` file in the `backend` folder:

```env
DATABASE_URL=postgresql://YOUR_USERNAME:YOUR_PASSWORD@localhost:5432/matchmytone
```

**Default connection (if username is `postgres` and password is `postgres`):**
```
postgresql://postgres:postgres@localhost:5432/matchmytone
```

## Step 4: Verify PostgreSQL is Running

1. **Check if PostgreSQL service is running:**
   - Press `Win + R`
   - Type `services.msc` and press Enter
   - Look for "postgresql-x64-15" (or your version)
   - Make sure it's "Running"

2. **If not running:**
   - Right-click on the service → "Start"

## Step 5: Run Your Backend

```bash
cd backend
python app.py
```

The app will automatically create all the tables when it starts!

## Troubleshooting

### "Connection refused" error:
- Make sure PostgreSQL service is running (see Step 4)
- Check if port 5432 is correct
- Verify username and password

### "Database does not exist" error:
- Make sure you created the `matchmytone` database (Step 2)

### "Password authentication failed":
- Check your `.env` file or update the connection string in `app.py`
- Make sure username and password are correct

## Quick Test

To test if PostgreSQL is working, run:
```bash
psql -U postgres -d matchmytone
```

If it connects successfully, you're all set! 🎉





























