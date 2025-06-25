-- Create the database (if not already created)
CREATE DATABASE IF NOT EXISTS fitness_app;
USE fitness_app;

-- Create users table
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  age INT,
  gender VARCHAR(10),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create member_sessions table
CREATE TABLE IF NOT EXISTS member_sessions (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  weight_kg DECIMAL(5,2),
  height_m DECIMAL(4,2),
  max_bpm INT,
  avg_bpm INT,
  resting_bpm INT,
  session_duration_hours DECIMAL(4,2),
  calories_burned DECIMAL(6,2),
  workout_type VARCHAR(50),
  fat_percentage DECIMAL(4,1),
  water_intake_liters DECIMAL(4,2),
  workout_frequency_days INT,
  experience_level INT,
  bmi DECIMAL(5,2),
  recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);
