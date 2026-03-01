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


Here is your **visually styled, professional GitHub README** with badges, banner style header, clean formatting, and recruiter-attractive structure.

You can **directly copy-paste this into README.md**.

---

# 🔐 Smart Door Unlock System

<p align="center">
  <b>A Secure Web-Based Smart Access Control System</b><br>
  Built with Flask • Real-Time Webcam Capture • Time-Bound OTP Verification
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-Web_Framework-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Database-SQLite-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">
</p>

---

## 🚀 Overview

Smart Door Unlock System is a **software-based smart security solution** that enables secure visitor authentication using:

* 📸 Real-time webcam capture
* 🔢 6-digit time-bound access code
* 🧾 Access logging with timestamps
* 🖥️ Owner dashboard verification

This project simulates an **IoT-based smart door system** completely through a web application.

---

## 🎯 Key Features

✅ Visitor Access Request System
✅ Real-Time Webcam Snapshot Capture
✅ Owner Dashboard for Approval
✅ Secure 6-Digit OTP Generation
✅ Time-Limited Code Verification
✅ Access History Logging
✅ Clean & Modern UI

---

## 🧠 Business Understanding

Traditional lock systems rely on physical keys, which are:

* Easily lost
* Duplicated
* Not remotely manageable

This project solves that by implementing a **secure digital access workflow** where:

1. Visitor requests access
2. Owner verifies identity via snapshot
3. Owner shares temporary OTP
4. System validates and unlocks

This makes the system suitable for:

* Smart Homes
* Offices
* Hostels
* Gated Apartments

---

## 📊 Data Understanding

This project does not rely on external datasets.

Instead, it dynamically generates and manages:

* Visitor snapshots
* Secure 6-digit OTP
* Expiry timestamps
* Access logs (Success/Failure)

### Future Improvements

* Face Recognition Integration
* Email/SMS Notification
* Cloud Deployment (AWS/Render)
* Role-Based Authentication
* MongoDB / PostgreSQL Integration

---

## 🖼️ Screenshots

> Create a folder named `screenshots` in your repo and place images there.

### 📸 Visitor Access Page

```
![Visitor Page](screenshots/visitor.png)
```

### 🖥️ Owner Dashboard

```
![Owner Dashboard](screenshots/owner.png)
```

### 📋 Access Logs

```
![Access Logs](screenshots/logs.png)
```

---

## 🛠️ Tech Stack

### 🔹 Backend

* Python
* Flask
* Jinja2

### 🔹 Frontend

* HTML5
* CSS3
* JavaScript
* WebRTC (Webcam Access API)

### 🔹 Database

* SQLite

---

## ⚙️ Installation & Setup

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

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🔄 System Workflow

```
Visitor → Capture Snapshot → Send Request → 
Owner Dashboard → Generate OTP → 
Visitor Enters OTP → Server Validation → 
Access Granted / Denied → Log Stored
```

### 🔐 Security Logic

* Random 6-digit code generation
* Server-side verification
* Expiry validation
* Access attempt logging

---

## 📂 Project Structure

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

## 📌 Status

🟢 Completed
🔄 Open for Enhancements

---

## 💡 Why This Project is Valuable

This project demonstrates:

* Full-Stack Development
* Real-Time Media Handling
* Secure Backend Logic
* Authentication Workflow
* Practical IoT Simulation
* Clean UI Implementation

It reflects strong skills in **Python, Flask, and secure system design**.

---

## 🙌 Author

Developed as a full-stack smart security system project.
