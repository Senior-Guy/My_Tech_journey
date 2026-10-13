# My Tech Journey

This repository is my Python learning space. I’m documenting my progress as I build foundational programming skills with hands-on exercises, small projects, and API development.

## Purpose

The goal is simple: learn by doing.

I’m practicing:
- Python syntax and logic
- conditionals and decision-making
- functions and reusable code
- validation and input checking
- problem-solving with small real-world scenarios
- building basic APIs with FastAPI

## Included Projects

### 1st labwork.py
A practical exercise using conditional logic to decide if a trip is possible based on distance, weather, and available transport.

### 2nd Lab.py
A small character creation function with validation rules for name length, stats, and total score constraints.

### 1st_fastapi.py
My first FastAPI project — a simple Student Management API.

**What it does:**
- `GET /` → Returns a welcome message
- `GET /get-student/{student_id}` → Get a student by ID
- `GET /get-by-name/{student_id}` → Search student by name
- `POST /create-student/{student_id}` → Create a new student
- `PUT /update-student/{student_id}` → Update student details
- `DELETE /delete-student/{student_id}` → Delete a student

**Technologies used:**
- FastAPI
- Pydantic (for data validation)
- Path parameters and optional query parameters
  
## How to Run
uvicorn 1st_fastapi:app --reload

### Basic Python scripts
```bash
python "1st labwork.py"
python "2nd Lab.py"
