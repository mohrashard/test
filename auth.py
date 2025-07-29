from flask import Blueprint, request, render_template, redirect, url_for
from models import users_collection

auth = Blueprint("auth", __name__)

@auth.route("/", methods=["GET"])
def signup_form():
    return render_template("signup.html")

@auth.route("/signup", methods=["POST"])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return "Please fill in all fields.", 400

    users_collection.insert_one({"username": username, "password": password})
    return f"User {username} signed up successfully!"
