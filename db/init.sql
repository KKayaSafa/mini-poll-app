CREATE DATABASE IF NOT EXISTS surveydb;
USE surveydb;

CREATE TABLE IF NOT EXISTS poll_responses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    q1 ENUM('agree', 'neutral', 'disagree'),
    q2 ENUM('agree', 'neutral', 'disagree'),
    q3 ENUM('agree', 'neutral', 'disagree'),
    q4 ENUM('agree', 'neutral', 'disagree'),
    q5 ENUM('agree', 'neutral', 'disagree'),
    q6 ENUM('agree', 'neutral', 'disagree'),
    q7 ENUM('agree', 'neutral', 'disagree'),
    q8 ENUM('agree', 'neutral', 'disagree'),
    q9 ENUM('agree', 'neutral', 'disagree'),
    q10 ENUM('agree', 'neutral', 'disagree')
);
