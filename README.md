# 🚀 AWS S3 Static Website Automation

Automated static website deployment on AWS S3 using Python (boto3). This project creates an S3 bucket, uploads a frontend website, enables static hosting, and configures public access without using the AWS console.

## 🎯 Overview
This project automates hosting of a static website on AWS. A Python script performs all steps including bucket creation, file upload, enabling hosting, and applying bucket policy.

## 🧰 Tech Stack
AWS S3 | Python (boto3) | HTML, CSS, JavaScript

## ⚙️ Steps Performed
1. Create S3 bucket  
2. Disable public access block  
3. Upload index.html  
4. Enable static website hosting  
5. Apply bucket policy  
6. Generate public website URL  

## 📂 Project Structure
aws-s3-static-website-automation/
 ├── index.html
 └── deploy.py

## ▶️ Run
pip install boto3  
aws configure  
python deploy.py  

## 🌐 Live Website
http://sayali-demo-site-2026-001.s3-website-ap-south-1.amazonaws.com

### 🪣 S3 Bucket Created & File Uploaded
![S3 Bucket](https://github.com/user-attachments/assets/d9a76951-fce9-49c1-a7b7-7df68d11f6fd)

### 🌍 Static Website Hosting Endpoint
![Hosting Endpoint](https://github.com/user-attachments/assets/ba9446e2-33af-401b-8a78-bd6bdda75691)

### ⚙️ Deployment Script Execution
![Script Run](https://github.com/user-attachments/assets/c3b18776-d95e-406a-8462-501a6ce04867)

### 🌐 Website Live
![Live Website](https://github.com/user-attachments/assets/1eab3d36-1339-492f-bb76-50c61364ac5f)

### ✅ Website Working Properly
![Working Website](https://github.com/user-attachments/assets/68c391e4-ab9f-416b-afde-bad03dcd9ef8)

---

## ✨ Features
✔ Automated deployment  
✔ No manual AWS console work  
✔ Static website hosting  
✔ Public access via bucket policy  



