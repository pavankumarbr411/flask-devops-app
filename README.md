# 🚀 DevOps Flask App with MongoDB

A full-stack web application using **Flask**, **MongoDB**, **Docker**, and **Jenkins CI/CD**. This project demonstrates backend logic, database operations, containerization, and automated deployment in one clean, DevOps-ready stack.

## 🌟 Features

- 🧩 Modular Flask backend architecture
- 🗃️ MongoDB integration via `flask-pymongo`
- 🛠️ Containerized with Docker
- 🔐 Environment-based configuration using `.env`
- 🧪 Unit testing with `pytest`
- 🔁 Jenkins CI/CD pipeline integration

## 💻 Tech Stack

| Tool          | Role                        |
|---------------|-----------------------------|
| Flask         | Backend web framework       |
| MongoDB       | NoSQL database              |
| Docker        | Containerization            |
| Jenkins       | Continuous Integration/Delivery |
| Python        | Language                    |
| Pytest        | Testing framework           |

## 🛠️ Getting Started

```bash
# Clone the repo
git clone https://github.com/pavankumarbr411/flask-devops-app.git
cd flask-devops-app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
# Create a .env file in the root directory:
MONGO_URI=your-mongo-uri
FLASK_APP=app
FLASK_ENV=development

# Run the app
flask run


🧪 Run Tests
pytest

🐳 Docker Setup
docker build -t flask-devops-app .
docker run -p 5000:5000 flask-devops-app

🔁 Jenkins CI/CD
Jenkinsfile automates testing, building, and deployment

Connect your GitHub repo with Jenkins for full automation

🙋‍♂️ Author
Pavan Kumar B R 
