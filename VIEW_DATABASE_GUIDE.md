# 📊 How to View Your PostgreSQL Database

## Option 1: Using pgAdmin (GUI - Recommended for Beginners)

### Step 1: Open pgAdmin

1. **Press Windows key** and search for "pgAdmin 4"
2. **Click on pgAdmin 4** to open it
3. **Enter your PostgreSQL password** when prompted (password: `MatchMyTone`)

### Step 2: Navigate to Your Database

1. In the left panel, expand:
   - **Servers** → **PostgreSQL 16** (or your version)
   - **Databases** → **matchmytone**
   - **Schemas** → **public** → **Tables**

2. You should see tables like:
   - `users` - Contains all registered users
   - `quiz_results` - Contains all quiz results

### Step 3: View the Users Table

1. **Right-click on `users` table**
2. **Select "View/Edit Data" → "All Rows"**
3. You'll see all registered users with their data:
   - id
   - name (username)
   - email
   - phone
   - password (hashed - not readable)
   - gender
   - dob
   - age
   - created_at
   - updated_at

### Step 4: View Quiz Results Table

1. **Right-click on `quiz_results` table**
2. **Select "View/Edit Data" → "All Rows"**
3. You'll see all quiz results saved by users

---

## Option 2: Using Command Line (psql)

### Step 1: Open Command Prompt

### Step 2: Connect to PostgreSQL

```bash
psql -U postgres -d matchmytone
```

Enter password: `MatchMyTone`

### Step 3: View Users Table

```sql
SELECT * FROM users;
```

This will show all users. For better formatting:

```sql
SELECT id, name, email, phone, gender, dob, age, created_at FROM users;
```

### Step 4: View Quiz Results

```sql
SELECT * FROM quiz_results;
```

### Step 5: Exit psql

```sql
\q
```

---

## Quick Commands

### See all tables in database:
```sql
\dt
```

### See structure of users table:
```sql
\d users
```

### See specific user (e.g., Vanshita11):
```sql
SELECT * FROM users WHERE name = 'Vanshita11';
```

### Count total users:
```sql
SELECT COUNT(*) FROM users;
```

---

## ✅ What You Should See

Based on your logs, you should see:
- User: `Vanshita11` in the users table
- Multiple quiz results in quiz_results table (skincare, body-shape, face-shape)

All your data is being stored successfully! 🎉



















