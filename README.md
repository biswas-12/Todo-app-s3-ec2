# TaskTracker 📝

TaskTracker is a full-stack To-Do management application built using React (Frontend) and Django REST Framework (Backend).
The project showcases clean architecture, Docker-based packaging, and real-world production deployment using AWS services.

---

## 🎯 Aim of the Project

The primary objective of this project is to demonstrate a **modern, decoupled cloud architecture** by deploying a full-stack application on AWS using a split-deployment strategy. Instead of hosting everything on a single server, this project separates the frontend and backend to achieve higher scalability, maintainability, and performance.

The React-based frontend is deployed using **AWS S3 Static Website Hosting**, which provides:
- Ultra-fast content delivery  
- Zero server maintenance  
- Low-cost hosting for static files

The Django REST API runs inside a **Docker container on an AWS EC2 instance**, ensuring:

- A consistent and isolated runtime environment  
- Easy portability for future cloud deployments  
- Simplified deployment through containerization
  
---

## 🚀 Features

- Create new tasks quickly  
- View the list of existing tasks  
- Mark tasks as completed / crossed-off  
- Delete tasks you no longer need  
- Clean UI with gradient backgrounds & responsive design  
- REST API backend with Dockerised deployment  

---

## 🧩 Tech Stack

- **Frontend:** React (Axios for HTTP)  
- **Backend:** Django REST Framework  
- **Docker:** Containerised both frontend and backend  
- **Deployment:** Frontend on AWS S3, Backend on AWS EC2  

---

## 🚀 Deployment Steps (Backend on EC2 + Frontend on S3)

This project uses a decoupled architecture:
- **Frontend (React)** → AWS **S3 Static Hosting**
- **Backend (Django + Docker)** → AWS **EC2**

---

# 🚀 Deployment Steps

## 🔹 Phase 1: Deploy Backend on EC2

### 1. Launch EC2 Instance
- Ubuntu 22.04    
- Open ports: **22**, **8000**

### 2. Install Docker & Git
```bash
sudo apt update
sudo apt install docker.io git -y
sudo usermod -aG docker $USER
```

### 3. Clone Backend
```bash
git clone "https://github.com/biswas-12/Todo-app-s3-ec2.git"
cd Backend
```

Set:
```python
ALLOWED_HOSTS = ["---EC2 Public IP---"]
```

### 4. Build & Run Docker
```bash
docker build -t django-app .
docker run -d -p 8000:8000 django-app
```

---

## 🔹 Phase 2: Deploy Frontend on S3

### 1. Set API URL
```js
const API_URL = "http://<EC2-IP>:8000/api";
```

### 2. Build React App
```bash
npm install
npm run build
```

### 3. Create S3 Bucket & Enable Static Hosting  
Index: `index.html`  
Error: `index.html`

### 4. Upload Build Files
- Upload all the contents of your local build folder (not the folder itself, but the files inside build folder like index.html, static, etc.).

### 5. Add Public Policy
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::YOUR-BUCKET/*"
  }]
}
```

---

## 🔹 Phase 3: Fix CORS (Backend)

Add in Django:
```python

CORS_ALLOWED_ORIGINS = [
    "http://<your-s3-endpoint>"
]
```

Rebuild:
```bash
docker build -t django-app .
docker run -d -p 8000:8000 django-app
```

---

# ✔️ Final Result
- Frontend → Live on S3  
- Backend → Running on EC2  
- API fully connected with CORS  
