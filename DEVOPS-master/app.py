from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

from models.user_model import UserModel
from models.task_model import TaskModel

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Secret key for session
app.secret_key = os.getenv("SECRET_KEY")

# MongoDB configuration
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

# Initialize PyMongo and models
mongo = PyMongo(app)
user_model = UserModel(mongo)
task_model = TaskModel(mongo)

# Home route redirects to login
@app.route("/")
def home():
    return redirect(url_for("login"))

# Signup route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            flash("Passwords do not match!")
            return redirect(url_for("signup"))

        if user_model.find_by_username(username):
            flash("Username already exists!")
            return redirect(url_for("signup"))

        user_model.create_user(username, password)
        flash("Signup successful! Please login.")
        return redirect(url_for("login"))

    return render_template("signup.html")

# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if user_model.verify_user(username, password):
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid username or password"
            return render_template("login.html", error=error)

    return render_template("login.html")

# Logout route
@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out.")
    return redirect(url_for("login"))

# Dashboard route
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    tasks = task_model.get_tasks(session["user"])
    completion = task_model.get_completion_percentage(tasks)

    return render_template("dashboard.html", tasks=tasks, completion_percentage=completion)

# Add task route
@app.route("/add", methods=["POST"])
def add_task():
    if "user" in session:
        task_text = request.form["task"]
        start_time = request.form.get("start_time") or None
        end_time = request.form.get("end_time") or None
        
        # Ensure the datetime values are in the correct format (if needed, add additional processing)
        task_model.add_task(session["user"], task_text, start_time, end_time)
    
    return redirect(url_for("dashboard"))

# Mark task as complete
@app.route("/complete/<task_id>")
def complete_task(task_id):
    task_model.complete_task(task_id)
    return redirect(url_for("dashboard"))

# Delete task
@app.route("/delete/<task_id>")
def delete_task(task_id):
    task_model.delete_task(task_id)
    return redirect(url_for("dashboard"))

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
