🧠 AI Log Monitoring System

A Dockerized AI-powered log monitoring system that detects anomalous system logs using Machine Learning and visualizes results through a Flask web dashboard.

🚀 Features

- 🔍 AI-based anomaly detection using Isolation Forest
- 🌐 Web dashboard built with Flask
- 📦 Fully Dockerized for easy deployment
- 📊 Real-time log classification (Normal / Anomaly)
- 🧪 Simple and extensible architecture for DevOps integration 
   
🏗️ Architecture

User → Flask Web App → ML Model (Isolation Forest) → Prediction → UI Dashboard 


🧰 Tech Stack

- Python 🐍
- Flask 🌐
- Scikit-learn 🤖
- Pandas / NumPy 📊
- Docker 🐳
- Git & GitHub


📁 Project Structure

ai-log-monitor/
│
├── app/
│ └── app.py # Flask web application
│
├── model/
│ └── model.py # ML model (Isolation Forest)
│
├── requirements.txt # Dependencies
├── Dockerfile # Container configuration
└── README.md


⚙️ Setup Instructions

🔹 1. Clone the repository
  git clone https://github.com/JeyAakash/ai-log-monitor.git
  cd ai-log-monitor
🔹 2. Create virtual environment (optional)
  python -m venv venv
  venv\Scripts\activate   # Windows
🔹 3. Install dependencies
  pip install -r requirements.txt
🔹 4. Run Flask app
  python app/app.py

Open in browser:

http://127.0.0.1:5000
🐳 Run using Docker
🔹 Build image
  docker build -t ai-log-monitor .
🔹 Run container
  docker run -p 5000:5000 ai-log-monitor
