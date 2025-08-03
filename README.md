# visitor_log_system

A web-based application that allows security guards to log visitor details and store them securely in a MySQL database. Built using *Python, **Flask, and **MySQL*, this system provides a simple interface for entering visitor data like name, mobile number, and flat number.

---

## 🔧 Tech Stack

- *Frontend:* HTML, CSS
- *Backend:* Python (Flask)
- *Database:* MySQL
- *Libraries Used:* Flask, flask-mysqldb, datetime

---

## 🚀 Features

- Home page for navigation
- Visitor log form for name, mobile, flat number
- Data stored in MySQL database (visitor_log table)
- Success confirmation page
- Static background image used (bg.jpg)

---

## 📁 Folder Structure
. . .

📁 visitor_log_system/
├── app.py
├── static/bg.jpg
├── templates/home.html
├── templates/log.html
├── templates/success.html
├── requirements.txt
└── README.md
. . .
---

## 💻 How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/visitor_log_system.git
cd visitor_log_system

2. (Optional) Create a virtual environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Set up MySQL
	•	Open your MySQL client and run:

CREATE DATABASE society_log;

USE society_log;

CREATE TABLE visitor_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    mobile VARCHAR(15),
    flat VARCHAR(10),
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

5. Run the Flask app

python app.py

Then visit:
http://127.0.0.1:5000 in your browser.

⸻

🧠 Notes
	•	Database credentials are hardcoded in app.py. You can improve this using environment variables in production.
	•	Visitor data is inserted via the /log route using POST requests from an HTML form.
	•	You can style your templates using bg.jpg located inside the static folder.

⸻

📌 Author

K Prathamesh Nayak

⸻

📎 GitHub Repository

🔗 visitor_log_system

⸻

✅ Status

Project Completed ✅ — Ready for Resume/Portfolio.
