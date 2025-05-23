# 🗳️ Mini Survey App with Flask & MySQL

This is a simple survey web application built using **Flask** (Python) and **MySQL**, fully containerized with **Docker Compose**.  
Users can respond to 10 predefined questions using radio buttons: **Agree**, **Neutral**, or **Disagree**. Their answers are stored in a MySQL database.

---

## 📦 Features

- ✅ 10-question survey form
- ✅ Radio button options for each question
- ✅ Responses saved to MySQL
- ✅ Dockerized architecture (Flask + MySQL in separate containers)
- ✅ Uses `.env` for secure configuration

---

## ⚙️ Tech Stack

- **Backend**: Python 3.12 + Flask
- **Database**: MySQL 8
- **Containerization**: Docker & Docker Compose
- **Environment Configuration**: python-dotenv

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mini-poll-app.git
cd mini-poll-app

### 2. Create a .env file in the project root:

MYSQL_ROOT_PASSWORD=rootpass
MYSQL_DATABASE=surveydb
MYSQL_USER=surveyuser
MYSQL_PASSWORD=surveypass

### 3. Build and run with Docker Compose

docker-compose up --build

### 4. Access the web app

http://localhost:5000