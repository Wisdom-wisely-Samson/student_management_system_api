# Student Management API

## Overview

The **Student Management API** is a RESTful backend application built with **Python** and **FastAPI** as part of a backend development learning project. The application demonstrates modern backend architecture and best practices, including API development, request validation, routing, service layers, and database integration.

This project is designed to evolve from a simple CRUD application into a production-ready backend that can serve web, mobile, and desktop applications.

---

## Objectives

The main objectives of this project are to:

* Learn modern backend development with FastAPI.
* Understand REST API principles.
* Build a clean and scalable backend architecture.
* Perform CRUD (Create, Read, Update, Delete) operations.
* Validate incoming requests using Pydantic.
* Store and retrieve data using SQLAlchemy and SQLite.
* Prepare the project for migration to PostgreSQL and deployment.

---

## Features

### Current Features

* RESTful API built with FastAPI
* Automatic interactive API documentation using Swagger UI
* Student creation
* Retrieve all students
* Request validation using Pydantic
* SQLAlchemy ORM integration
* SQLite database persistence
* Layered architecture (Routers, Services, Models, Schemas)
* Automatic database table creation

---

## Technologies Used

* Python 3
* FastAPI
* Uvicorn
* Pydantic
* SQLAlchemy
* SQLite

---

## Project Structure

```text
student_api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   │
│   ├── models/
│   │   └── student.py
│   │
│   ├── schemas/
│   │   └── student.py
│   │
│   ├── services/
│   │   └── student_service.py
│   │
│   └── routers/
│       └── student_router.py
│
├── student.db
├── requirements.txt
├── README.md
└── venv/
```

---

## Architecture

The application follows a layered architecture that separates responsibilities into different components.

```text
Client
   │
   ▼
Router
   │
   ▼
Service
   │
   ▼
SQLAlchemy Model
   │
   ▼
SQLite Database
```

### Components

* **Routers** handle incoming HTTP requests.
* **Services** contain business logic.
* **Schemas** validate request and response data using Pydantic.
* **Models** represent database tables using SQLAlchemy.
* **Database** manages connections and sessions.

---

## API Endpoints

| Method | Endpoint    | Description           |
| ------ | ----------- | --------------------- |
| GET    | `/`         | API Welcome Message   |
| GET    | `/students` | Retrieve all students |
| POST   | `/students` | Create a new student  |

---

## Running the Project

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Environment

Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Server

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

OpenAPI Schema:

```text
http://127.0.0.1:8000/openapi.json
```

---

## Learning Outcomes

This project demonstrates practical knowledge of:

* Python programming
* Object-Oriented Programming (OOP)
* REST API development
* FastAPI framework
* HTTP methods
* JSON data exchange
* Pydantic validation
* SQLAlchemy ORM
* SQLite database integration
* Layered software architecture
* Dependency Injection
* CRUD operations

---

## Future Improvements

The project will continue to evolve with additional backend features, including:

* Retrieve a student by ID
* Update student information
* Delete students
* PostgreSQL database integration
* Alembic database migrations
* JWT Authentication
* Role-Based Access Control (RBAC)
* Pagination and filtering
* Search functionality
* Logging
* Environment variable management
* Unit and integration testing
* Docker containerization
* Deployment to a cloud platform

---

## Purpose

This project serves as a learning milestone in mastering professional backend development with Python and FastAPI. The knowledge and architecture developed here provide the foundation for building larger production systems such as School Management Systems, Business Management Platforms, SaaS applications, and enterprise REST APIs.

---

## Author

**Wisdom Wisely Samson**

Backend Developer | Software Engineering Learner | Aspiring Full-Stack Developer

---

## License

This project is open for educational and personal learning purposes.
