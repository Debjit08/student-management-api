
CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll VARCHAR(20),
    name VARCHAR(100),
    dob DATE,
    class_name VARCHAR(50)
);
