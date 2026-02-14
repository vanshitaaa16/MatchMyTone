-- SQL Query to create color_analysis_results table
-- Run this in your PostgreSQL database

CREATE TABLE IF NOT EXISTS color_analysis_results (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    photo_uri VARCHAR(500),
    season_type VARCHAR(100),
    season_description TEXT,
    undertone VARCHAR(50),
    undertone_description TEXT,
    colors_to_wear JSONB,
    colors_to_avoid JSONB,
    is_face BOOLEAN DEFAULT TRUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create index on user_id for faster queries
CREATE INDEX IF NOT EXISTS idx_color_analysis_user_id ON color_analysis_results(user_id);

-- Create index on created_at for sorting
CREATE INDEX IF NOT EXISTS idx_color_analysis_created_at ON color_analysis_results(created_at DESC);

-- Add comment to table
COMMENT ON TABLE color_analysis_results IS 'Stores color analysis results from Gemini API analysis';








