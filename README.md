# 🚀 Automated CI/CD Pipeline with Google Cloud Build & GKE
This project demonstrates how to build, containerize, and deploy a full-stack Todo App to Google Kubernetes Engine (GKE) with an automated CI/CD pipeline using Google Cloud Build Triggers.

![GCP_PROJECT drawio](https://github.com/user-attachments/assets/c91d3c4a-17b3-4a54-8a8e-4ab307837648)


## 📍 Overview
This app is a simple full-stack Todo Tracker built with React (Frontend) and Django (Backend).
It is deployed on GKE, and the CI/CD pipeline is fully automated using Google Cloud services.
Any changes made in the GitHub repository automatically trigger a build and deploy pipeline.

### 🎯 Features:
 - ✅ Full-stack Todo app with CRUD functionality
 - ✅ Containerized using Docker
 - ✅ Deployed on GKE with a LoadBalancer service
 - ✅ GitHub → Cloud Build Trigger → Artifact Registry → GKE (CI/CD)

### 🛠️ Tech Stack:
 - ⚙️ Backend: Django, Django REST Framework
 - 🎨 Frontend: React.js
 - 🐳 Containers: Docker

### ☁️ Cloud Services:
 - Google Cloud Build
 - Google Artifact Registry
 - Google Kubernetes Engine (GKE)

## 🚀 How to Implement

Follow the steps below to build and deploy this app with an automated CI/CD pipeline on Google Cloud using **Cloud Build**, **Artifact Registry**, and **GKE**.

---

### 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/biswas-12/Todo-App-using-GCP-CICD.git
```

### 🔗 Step 2: Create a Cloud Build Trigger
 - Navigate to **Cloud Build > Triggers** in the Google Cloud Console.
 - Connect your GitHub repository.
 - Set the trigger to activate on push to main branch (or your desired branch).

### 📦 Step 3: Add cloudbuild.yaml File
This file is used by Cloud Build to:
 - Build the Docker image
 - Push it to Google Artifact Registry

### ✅ Step 4: Commit Code
After pushing code to the configured branch, Cloud Build will automatically trigger and start the build process.

### 📁 Step 5: Add Kubernetes Manifests
Create Kubernetes YAML files inside a /k8s folder:
 - frontend-deployment.yaml
 - backend-deployment.yaml
   
Define both deployement and services in each.

### 🔄 Step 6: Update cloudbuild.yaml to Deploy
Add kubectl deployment steps to your cloudbuild.yaml:

### 🌀 Step 7: Push Updated Code Again
Once you commit your Kubernetes manifests and updated cloudbuild.yaml, Cloud Build will:
 - Build and push your Docker image
 - Deploy it to GKE


### 🌐 Step 8: Access Your Application
 - Get the external IP from the Kubernetes service:
 - Visit your frontend and backend in the browser using that IP!

