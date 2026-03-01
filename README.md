The **Secure Entry System using Flask and WebRTC** is a web-based visitor authentication
platform designed to enhance access control in residential and commercial settings. Visitors
request access through a web interface, where their webcam snapshot is captured using WebRTC
technology and securely transmitted to the owner’s dashboard. The owner can review the request
in real time and provide a unique, time-bound access code. This code is then verified on the
visitor’s interface via a Flask backend, ensuring secure and controlled entry. The system maintains
an access history log with timestamps and verification results for auditing purposes. By combining
lightweight server-side processing with modern browser-based media capture, the project delivers
a cost-effective, scalable, and user-friendly solution for secure entry management.

Keywords: Secure Entry System, Flask framework, WebRTC, Web-based access control, Visitor
authentication, Real-time communication, Time-bound access code, Snapshot verification, Access
history logging.


# 🔐 Smart Door Unlock System

<p align="center">
  <img src="https://img.shields.io/badge/Smart-Security_System-blueviolet?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/mdaliuddinhyder04/Smart-Door-Unlock?style=for-the-badge">
  <img src="https://img.shields.io/github/forks/mdaliuddinhyder04/Smart-Door-Unlock?style=for-the-badge">
  <img src="https://img.shields.io/github/issues/mdaliuddinhyder04/Smart-Door-Unlock?style=for-the-badge">
  <img src="https://img.shields.io/github/license/mdaliuddinhyder04/Smart-Door-Unlock?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Production_Ready-brightgreen?style=for-the-badge">
</p>

<p align="center">
<b>A Secure Full-Stack Smart Access Control System Built with Flask</b><br>
Real-Time Webcam Capture • OTP-Based Authentication • Access Logging • IoT Simulation
</p>

---

# 🚀 Project Overview

The **Smart Door Unlock System** is a full-stack web application that simulates an IoT-based smart access control mechanism.

It enables secure visitor verification through:

* 📸 Real-time webcam snapshot capture
* 🔢 Secure 6-digit time-bound OTP generation
* 🖥 Owner dashboard verification system
* 🧾 Access attempt logging with timestamps

This project demonstrates practical implementation of **authentication systems, secure backend validation, and real-time media handling** using modern web technologies.

---

# 🎯 Core Features

✔ Visitor Access Request Interface
✔ Real-Time Webcam Integration (Browser Media API)
✔ Owner Verification Dashboard
✔ Random Secure OTP Generation
✔ Time-Based Expiry Validation
✔ Server-Side Authentication
✔ Access History Logging
✔ Clean, Modern UI

---

# 🧠 Business Understanding

Traditional access systems rely on physical keys or static passwords, which:

* Can be lost or duplicated
* Cannot be remotely controlled
* Provide no real-time monitoring

This project solves these problems by implementing a **secure, software-based smart access workflow**.

### System Logic

1. Visitor requests access
2. System captures live snapshot
3. Owner reviews visitor identity
4. Owner generates temporary OTP
5. Visitor enters OTP
6. Server validates OTP & expiration
7. System logs the result

This architecture makes it suitable for:

* Smart Homes
* Office Security
* Hostel/Gated Community Access
* Remote Entry Systems

---

# 🏗 System Architecture

```
Visitor (Frontend)
        ↓
Webcam Snapshot (WebRTC)
        ↓
Flask Backend
        ↓
Owner Dashboard
        ↓
OTP Generation & Expiry
        ↓
Validation Engine
        ↓
Access Logs (SQLite)
```

---

# 🛠 Tech Stack

### 🔹 Backend

* Python
* Flask
* Jinja2
* SQLite

### 🔹 Frontend

* HTML5
* CSS3
* JavaScript
* WebRTC API

### 🔹 Security Logic

* Randomized 6-digit OTP
* Server-side validation
* Expiry time enforcement
* Attempt logging mechanism

---

# 📂 Project Structure

```
Smart-Door-Unlock/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── owner.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation Guide (Local Setup)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/mdaliuddinhyder04/Smart-Door-Unlock.git
cd Smart-Door-Unlock
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run Application

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

# 🌐 Deployment Guide

## 🚀 Deploy on Render

1. Push repository to GitHub
2. Go to [https://render.com](https://render.com)
3. Create “New Web Service”
4. Connect GitHub repo
5. Set:

   * Runtime: Python 3
   * Start Command: `python app.py`
6. Deploy

---

## 🚀 Deploy on Railway

1. Visit [https://railway.app](https://railway.app)
2. Create new project
3. Connect GitHub repository
4. Add environment variables if needed
5. Deploy

---

## 🚀 Deploy on AWS (EC2)

1. Launch EC2 instance
2. Install Python & Git
3. Clone repository
4. Install requirements
5. Run Flask app using:

   ```
   gunicorn app:app
   ```
6. Configure Nginx reverse proxy

---

# 🔄 Detailed Workflow

### Step 1 – Visitor Request

Visitor enters details and clicks request.

### Step 2 – Snapshot Capture

WebRTC captures real-time image.

### Step 3 – Owner Review

Owner dashboard displays visitor image.

### Step 4 – OTP Generation

System generates random 6-digit secure code.

### Step 5 – Expiry Logic

Code expires after defined time.

### Step 6 – Verification

Visitor enters OTP → Server validates.

### Step 7 – Logging

Access result stored in database with timestamp.

---

# 📊 Engineering Highlights (ATS Optimized)

* Full-stack web application development
* RESTful routing implementation
* Secure authentication workflow
* Session management
* Real-time browser media integration
* Backend validation logic
* SQLite database logging
* Clean UI architecture

---

# 🔐 Security Considerations

* Server-side OTP validation
* Expiry enforcement
* No client-side trust
* Controlled dashboard access
* Attempt tracking

---

# 📌 Project Status

✅ Completed
🚀 Deployment Ready
🔄 Open for Enhancements

---

# 🔮 Future Enhancements

* Face Recognition Integration (OpenCV / ML)
* Email / SMS OTP Delivery
* Role-Based Authentication
* Cloud Database (PostgreSQL)
* Mobile App Integration
* Docker Containerization

---

# 💼 Why This Project Stands Out

This project demonstrates:

* Strong backend logic design
* Secure authentication implementation
* Real-world IoT system simulation
* Production-ready structure
* Clean separation of frontend and backend

It reflects solid capability for roles like:

* Associate Software Engineer
* Backend Developer
* Full-Stack Developer
* IoT Application Developer

---

# 🙌 Author

Developed as a full-stack security system project demonstrating practical implementation of authentication and access control mechanisms.
