-- Add email verification columns to users table
-- Run this in your PostgreSQL database
-- IMPORTANT: Run each ALTER TABLE separately, then run UPDATE

-- Step 1: Add email_verified column
ALTER TABLE users 
ADD COLUMN IF NOT EXISTS email_verified BOOLEAN DEFAULT FALSE NOT NULL;

-- Step 2: Add verification_token column
ALTER TABLE users 
ADD COLUMN IF NOT EXISTS verification_token VARCHAR(100) UNIQUE;

-- Step 3: Add verification_token_expires column
ALTER TABLE users 
ADD COLUMN IF NOT EXISTS verification_token_expires TIMESTAMP;

-- Step 4: Update existing users to have email_verified = true (so they can still login)
UPDATE users SET email_verified = TRUE;

