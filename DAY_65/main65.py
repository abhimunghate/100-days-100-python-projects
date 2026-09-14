# This is Day 65 project : Portfolio Website Backend

import os
import json
from functools import wraps
from dotenv import load_dotenv
from werkzeug.security import check_password_hash
from flask import (Flask, render_template, request, redirect, url_for, session, flash)

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD_HASH = os.getenv("ADMIN_PASSWORD_HASH")

FEEDBACK_FILE = "feedback.json"

if not app.secret_key:
    raise RuntimeError("SECRET_KEY is missing from the .env file")

if not ADMIN_USERNAME or not ADMIN_PASSWORD_HASH:
    raise RuntimeError("ADMIN_USERNAME or ADMIN_PASSWORD is missing from the .env file")

def load_feedback():
    try:
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_feedback(name, email, message):
    feedbacks = load_feedback()
    normalized_email = email.strip().lower()
    
    for feedback in feedbacks:
        saved_email = feedback.get("email", "").strip().lower()
        
        if saved_email == normalized_email:
            return False
    
    feedback = {"name" : name.strip(), "email" : normalized_email, "message" : message.strip()}
    feedbacks.append(feedback)
    
    with open(FEEDBACK_FILE, "w", encoding="utf-8") as file:
        json.dump(feedbacks, file, indent=4)
    
    return True

def admin_required(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if not session.get("admin_logged_in"):
            return redirect(url_for("admin_login"))
        return function(*args, **kwargs)
    return decorated_function

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit-feedback", methods=["POST"])
def submit_feedback():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()
    
    if not name or not email or not message:
        flash("All fields are required.", "error")
        return redirect(url_for("contact"))
    
    if not save_feedback(name, email, message):
        flash("Feedback from this email address has already been submitted.", "error")
        return redirect(url_for("contact"))
    
    flash("Feedback submitted successfully!", "success")
    return redirect(url_for("contact"))

@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        
        valid_username = username == ADMIN_USERNAME
        valid_password = check_password_hash(ADMIN_PASSWORD_HASH, password)

        if valid_username and valid_password:
            session["admin_logged_in"] = True
            flash("Admin login successful.", "success")
            return redirect(url_for("view_feedback"))

        flash("Invalid username or password.", "error")
    return render_template("login.html")
        
@app.route("/feedback")
@admin_required
def view_feedback():
    search_query = request.args.get("search", "").strip().lower()
    feedbacks = load_feedback()

    if search_query:
        feedbacks = [feedback for feedback in feedbacks
            if search_query in feedback.get("name", "").lower()
            or search_query in feedback.get("email", "").lower()
            or search_query in feedback.get("message", "").lower()
        ]
    return render_template("feedback.html", feedbacks=feedbacks, search_query=search_query)

@app.route("/logout")
def logout():
    session.pop("admin_logged_in", None)
    flash("You have been logged out.", "success")
    return redirect(url_for("admin_login"))

if __name__ == "__main__":
    app.run(debug=True)
    
# Done