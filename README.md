# Student Management REST API

## Project Objective

The Student Management REST API is a backend application developed using Flask and SQLite.

It provides REST API endpoints to create, read, update, and delete student records. The project also includes input validation and API key authentication.

## Technologies Used

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* Postman
* Git and GitHub

## Features

* REST API
* CRUD operations
* SQLite database integration
* Input validation
* API key authentication
* Postman API testing

## Project Structure

```text
Student_Management_REST_API/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── Student_Management_API.postman_collection.json
```

The SQLite database is created locally when the application runs.

## Installation

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

For Git Bash:

```bash
source venv/Scripts/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

Set the API key as an environment variable:

```bash
export API_KEY="your-api-key"
```

Then run:

```bash
python -m flask --app app run --host=127.0.0.1 --port=5000
```

The API runs at:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint         | Description      |
| ------ | ---------------- | ---------------- |
| GET    | `/`              | Check API status |
| POST   | `/students`      | Add a student    |
| GET    | `/students`      | Get all students |
| PUT    | `/students/<id>` | Update a student |
| DELETE | `/students/<id>` | Delete a student |

## Authentication

The student endpoints use API key authentication.

Add this header in Postman:

```text
X-API-Key: your-api-key
```

Requests without the correct API key return HTTP status `401`.

Example response:

```json
{
    "error": "Invalid or missing API key"
}
```

## Validation

The API validates student information.

* Name is required.
* Branch is required.
* Year must be an integer from 1 to 4.

Invalid data returns HTTP status `400`.

Example request:

```json
{
    "name": "Test Student",
    "branch": "ECE",
    "year": 10
}
```

Example response:

```json
{
    "error": "Year must be an integer from 1 to 4"
}
```

## Database

SQLite is used to store student records.

Flask-SQLAlchemy is used for database integration and CRUD operations.

## CRUD Operations

### Create

A `POST` request to `/students` creates a new student record.

### Read

A `GET` request to `/students` retrieves student records.

### Update

A `PUT` request to `/students/<id>` updates an existing student.

### Delete

A `DELETE` request to `/students/<id>` deletes an existing student.

## API Testing

The API was tested using Postman.

Tested operations:

* POST - Create student
* GET - Read student
* PUT - Update student
* DELETE - Delete student
* Validation testing
* Authentication testing

## Testing Results

The REST API successfully performs CRUD operations with SQLite database integration.

Input validation and API key authentication were also implemented and tested using Postman.

## Future Improvements

* JWT-based authentication
* Better error handling
* User roles and permissions
* Frontend interface
* Cloud database integration
* API deployment

## Internship

This project was developed as part of the Python Development Internship – Week 2.

## API Testing Screenshots

### 1. GET - Read Students

![GET Students](Evidence/1-get-students.png)

### 2. POST - Create Student

![Create Student](Evidence/2-create-student.png)

### 3. PUT - Update Student

![Update Student](Evidence/3-update-student.png)

### 4. DELETE - Delete Student

![Delete Student](Evidence/4-delete-student.png)

### 5. Validation Testing

![Validation Error](Evidence/5-validation.png)

### 6. Authentication Testing

![Authentication Error](Evidence/6-authentication.png)