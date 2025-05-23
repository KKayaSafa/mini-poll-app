
# 🗳️ Mini Survey App with Flask & MySQL

A lightweight, containerized survey web application built with **Flask** and **MySQL** using **Docker Compose**.  
Users can answer 10 predefined questions using radio buttons (**Agree**, **Neutral**, **Disagree**), and their responses are stored in a MySQL database.

---

## 📦 Features

- ✅ 10-question survey form  
- ✅ Radio button options (Agree / Neutral / Disagree)  
- ✅ Responses stored in a MySQL database  
- ✅ Fully containerized using Docker Compose (Flask & MySQL in separate containers)  
- ✅ Secure configuration using a `.env` file  

---

## ⚙️ Tech Stack

- **Backend**: Python 3.12 + Flask  
- **Database**: MySQL 8  
- **Containerization**: Docker & Docker Compose  
- **Configuration Management**: python-dotenv  

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/KKayaSafa/mini-poll-app.git
cd mini-poll-app
```

### 2. Create a `.env` File

In the root of the project, create a file named `.env` and add the following:

```env
MYSQL_ROOT_PASSWORD=rootpass
MYSQL_DATABASE=surveydb
MYSQL_USER=surveyuser
MYSQL_PASSWORD=surveypass
```

### 3. Build and Run the Containers

```bash
docker-compose up --build
```

### 4. Access the Web Application

Open your browser and navigate to:

```
http://localhost:5000
```