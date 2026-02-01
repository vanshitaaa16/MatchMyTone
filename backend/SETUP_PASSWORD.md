# How to Fix PostgreSQL Password Error

## The Problem
The error `password authentication failed for user "postgres"` means the password in your connection string is wrong.

## The Solution

You need to update the `.env` file with your actual PostgreSQL password.

### Step 1: Find Your PostgreSQL Password
This is the password you entered when you installed PostgreSQL. If you don't remember it:

**Option A: Try common defaults:**
- `postgres`
- `admin`
- `password`
- `1234`

**Option B: Reset the password (if you forgot it):**
1. Open Command Prompt as Administrator
2. Run: `psql -U postgres`
3. If it asks for a password and you don't remember, you may need to reset it by editing PostgreSQL's authentication file (pg_hba.conf)

### Step 2: Update the .env File

1. Open `backend/.env` file
2. Find this line:
   ```
   DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/matchmytone
   ```
3. Replace `YOUR_PASSWORD` with your actual PostgreSQL password

**Example:**
If your password is `mypassword123`, the line should be:
```
DATABASE_URL=postgresql://postgres:mypassword123@localhost:5432/matchmytone
```

### Step 3: Make Sure the Database Exists

Before running the app, create the database:

**Using pgAdmin:**
1. Open pgAdmin 4
2. Enter your password
3. Right-click "Databases" → "Create" → "Database..."
4. Name: `matchmytone`
5. Click "Save"

**Using Command Line:**
```bash
psql -U postgres
```
Enter your password, then:
```sql
CREATE DATABASE matchmytone;
\q
```

### Step 4: Run Your Backend

```bash
cd backend
python app.py
```

It should work now! 🎉




















