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


Smart Door Unlock System

A secure web-based entry system built with Flask and WebRTC for real-time visitor authentication. Visitors request access via a browser; their webcam snapshot is captured and sent to the owner’s dashboard. The owner verifies the request and issues a unique time-bound access code. The system logs access history and results for audit and security.

🔗 Demo

(Add your live demo link here if available)
Example: https://your-demo-link.com

📌 Table of Contents

Business Understanding

Data Understanding

Screenshots

Technologies

Setup

Approach

Status

Credits

🧠 Business Understanding

This project was developed to solve the problem of secure remote access without relying on physical hardware locks. Traditional locks are vulnerable to lost keys, forced entry, or lack of remote control. This system enables real-time access authentication using a visitor’s webcam and unique access codes, making it ideal for residential and commercial use where safety and auditability matter.

You will learn how web communication, real-time media capture, backend code validation, and logging mechanisms are combined to build a secure entry workflow. Challenges include handling asynchronous media capture, validating access codes securely, and maintaining clean session logs.

📊 Data Understanding

There is no external dataset used in this project (since it is a web application). The system does collect temporary runtime data for:

Webcam snapshot captured via WebRTC

Time-bound access codes

Access logs with timestamps and results

If you expand this project in the future, you could integrate:

User database with roles (owner/guest)

Face recognition models

Cloud storage for logs and images

🖼️ Screenshots

(Include screenshots or GIFs of your UI views: visitor request page, owner dashboard, access approved/denied screens)

Example:




🛠️ Technologies

This project uses the following tools and frameworks:

Python – Core programming language

Flask – Backend web framework

WebRTC – Real-time webcam snapshot capture

HTML5 / CSS / JavaScript – Frontend user interface

SQLite – Lightweight database for logging

WebSockets/HTTP – Communication between frontend and backend

⚙️ Setup

Follow these steps to run the project locally:

Clone the repository

git clone https://github.com/mdaliuddinhyder04/Smart-Door-Unlock.git
cd Smart-Door-Unlock

Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Run the server

python app.py

Open the web app

Visit http://localhost:5000/visitor for visitor interface

Visit http://localhost:5000/owner for owner dashboard

(Adjust routes if your project uses different ones.)

🧠 Approach

The workflow of the project:

Visitor requests access from the web interface.

WebRTC captures webcam snapshot, which is sent to the backend.

Flask backend forwards the snapshot to the owner dashboard.

The owner reviews and validates the request.

The owner issues a unique access code with a time limit.

Visitor enters the code on their page for verification.

System logs each access attempt (success/failure + timestamp).

This structure blends modern browser APIs with secure backend logic to replace hardware-dependent access control.

📍 Status

Complete / Released – Functional system with real-time capture, validation, and logging.
You can update this if you add features like cloud deployment, face recognition, mobile support, etc.

💡 Credits

Thanks to:

Open-source contributors for Flask and WebRTC examples

GitHub community for UI inspiration
