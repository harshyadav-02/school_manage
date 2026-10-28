# School Management API

Simple CRUD API built with FastAPI, SQLAlchemy and PostgreSQL.

## Setup
1. Install PostgreSQL and create a database named `school_db`
2. Create a `.env` file with:
   DATABASE_URL=postgresql+psycopg://postgres:my_password@localhost:5432/school_db
3. pip install -r requirements.txt
4. uvicorn main:app --reload

## API Docs
http://127.0.0.1:8000/docs

## Endpoints
- POST /students
- GET /students
- GET /students/{id}
- PUT /students/{id}
- DELETE /students/{id}