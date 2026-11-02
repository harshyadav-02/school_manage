# School Management API

A simple CRUD API for managing students, built with **FastAPI**, **SQLAlchemy** and **PostgreSQL**.

## Features
- Create, read, update (PUT and PATCH) and delete students
- Data validation using Pydantic
- PostgreSQL database with SQLAlchemy ORM
- Duplicate email check
- Auto-generated API docs (Swagger UI)

## Tech Stack
- Python 3.10
- FastAPI and Uvicorn
- SQLAlchemy (ORM)
- Pydantic (validation)
- PostgreSQL
- python-dotenv

## Project Structure
```
school_manage/
|-- main.py            # API routes
|-- models.py          # Database table (SQLAlchemy)
|-- schemas.py         # Data validation (Pydantic)
|-- database.py        # Database connection
|-- requirements.txt   # Dependencies
|-- .env               # Secrets (not uploaded to GitHub)
```

## Setup
1. Install PostgreSQL and create a database named `school_db`
2. Clone the repo:
   ```
   git clone https://github.com/<your-username>/school_manage.git
   cd school_manage
   ```
3. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Create a `.env` file in the project folder:
   ```
   DATABASE_URL=postgresql+psycopg://postgres:your_password@localhost:5432/school_db
   ```
6. Run the server:
   ```
   uvicorn main:app --reload
   ```

## API Docs
Open http://127.0.0.1:8000/docs

## Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /students | Create a new student |
| GET | /students | Get all students |
| GET | /students/{id} | Get one student |
| PUT | /students/{id} | Update a student (all fields) |
| PATCH | /students/{id} | Update a student (only given fields) |
| DELETE | /students/{id} | Delete a student |

## Example Request
POST /students
```json
{
  "name": "Rahul Sharma",
  "email": "rahul@example.com",
  "age": 15,
  "student_class": "10th"
}
```