from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
API_KEY = os.getenv("API_KEY")
def require_api_key():
    key = request.headers.get("X-API-Key")

    if key != API_KEY:
        return {"error": "Invalid or missing API key"}, 401

    return None

# SQLite database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Student database model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    branch = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)


# Create database and table
with app.app_context():
    db.create_all()


# Home route
@app.route("/")
def home():
    return {"message": "Student Management API is running!"}

# Validate student data
def validate_student_data(data):
    if not data:
        return "Request body is required"

    if not isinstance(data.get("name"), str) or not data.get("name").strip():
        return "Name is required"

    if not isinstance(data.get("branch"), str) or not data.get("branch").strip():
        return "Branch is required"

    if not isinstance(data.get("year"), int) or data["year"] not in [1, 2, 3, 4]:
        return "Year must be an integer from 1 to 4"

    return None

# CREATE - Add a student
@app.route("/students", methods=["POST"])
def add_student():
    auth_error = require_api_key()

    if auth_error:
        return auth_error

    data = request.get_json()

    error = validate_student_data(data)

    if error:
        return {"error": error}, 400

    student = Student(
        name=data["name"],
        branch=data["branch"],
        year=data["year"]
    )

    db.session.add(student)
    db.session.commit()

    return {
        "id": student.id,
        "name": student.name,
        "branch": student.branch,
        "year": student.year
    }, 201


# READ - Get all students
@app.route("/students", methods=["GET"])
def get_students():
    auth_error = require_api_key()

    if auth_error:
        return auth_error

    students = Student.query.all()

    return [
        {
            "id": student.id,
            "name": student.name,
            "branch": student.branch,
            "year": student.year
        }
        for student in students
    ]


# UPDATE - Update a student
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    auth_error = require_api_key()

    if auth_error:
        return auth_error

    student = Student.query.get(student_id)

    if not student:
        return {"error": "Student not found"}, 404

    data = request.get_json()

    student.name = data["name"]
    student.branch = data["branch"]
    student.year = data["year"]

    db.session.commit()

    return {
        "id": student.id,
        "name": student.name,
        "branch": student.branch,
        "year": student.year
    }


# DELETE - Delete a student
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    auth_error = require_api_key()

    if auth_error:
        return auth_error

    student = Student.query.get(student_id)

    if not student:
        return {"error": "Student not found"}, 404

    db.session.delete(student)
    db.session.commit()

    return {"message": "Student deleted successfully"}


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)