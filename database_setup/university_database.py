
"""
SQLite university database schema definition and sample data seeder.
Run this file directly to create the database: python database_setup/university_database.py
"""

import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
UNIVERSITY_DB_PATH = DATA_DIR / "university.db"

CREATE_TABLES = [
    """CREATE TABLE IF NOT EXISTS departments (
        department_id   INTEGER PRIMARY KEY,
        department_name TEXT    NOT NULL,
        building        TEXT
    )""",
    """CREATE TABLE IF NOT EXISTS students (
        student_id      INTEGER PRIMARY KEY,
        student_name    TEXT    NOT NULL,
        city             TEXT,
        enrollment_year  INTEGER,
        department_id    INTEGER,
        FOREIGN KEY (department_id)
            REFERENCES departments(department_id)
    )""",
    """CREATE TABLE IF NOT EXISTS courses (
        course_id      INTEGER PRIMARY KEY,
        course_name    TEXT    NOT NULL,
        credits        INTEGER,
        department_id  INTEGER,
        FOREIGN KEY (department_id)
            REFERENCES departments(department_id)
    )""",
    """CREATE TABLE IF NOT EXISTS enrollments (
        enrollment_id INTEGER PRIMARY KEY,
        student_id    INTEGER,
        course_id     INTEGER,
        semester      TEXT,
        grade         REAL,
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    )""",
    """CREATE TABLE IF NOT EXISTS professors (
        professor_id   INTEGER PRIMARY KEY,
        professor_name TEXT    NOT NULL,
        department_id  INTEGER,
        salary         REAL,
        FOREIGN KEY (department_id)
            REFERENCES departments(department_id)
    )""",
]

DEPARTMENTS = [
    (1, "Computer Science", "Block A"),
    (2, "Business", "Block B"),
    (3, "Mechanical Engineering", "Block C"),
]

STUDENTS = [
    (101, "Arjun Rao", "Hyderabad", 2023, 1),
    (102, "Priya Shah", "Mumbai", 2022, 1),
    (103, "Rahul Verma", "Delhi", 2023, 2),
    (104, "Sneha Iyer", "Hyderabad", 2021, 3),
    (105, "Karan Mehta", "Pune", 2022, 2),
    (106, "Ananya Das", "Kolkata", 2024, 1),
]

COURSES = [
    (201, "Database Systems", 4, 1),
    (202, "Artificial Intelligence", 4, 1),
    (203, "Financial Accounting", 3, 2),
    (204, "Marketing Strategy", 3, 2),
    (205, "Thermodynamics", 4, 3),
]

ENROLLMENTS = [
    # (enrollment_id, student_id, course_id, semester, grade)
    (1, 101, 201, "2025-Fall", 88),
    (2, 101, 202, "2025-Fall", 92),
    (3, 102, 201, "2025-Fall", 76),
    (4, 102, 202, "2025-Fall", 81),
    (5, 103, 203, "2025-Fall", 85),
    (6, 103, 204, "2025-Fall", 79),
    (7, 104, 205, "2025-Fall", 91),
    (8, 105, 203, "2025-Fall", 68),
    (9, 105, 204, "2025-Fall", 74),
    (10, 106, 201, "2025-Fall", 95),
    (11, 106, 202, "2025-Fall", 89),
]

PROFESSORS = [
    (301, "Dr. Meera Nair", 1, 95000),
    (302, "Dr. Vikram Joshi", 2, 88000),
    (303, "Dr. Thomas Paul", 3, 91000),
]


def init_university_db():
    """Create tables and seed sample data if the database is empty."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(UNIVERSITY_DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    for stmt in CREATE_TABLES:
        cursor.execute(stmt)
    conn.commit()

    # Only seed if tables are empty
    if cursor.execute(
        "SELECT COUNT(*) FROM departments"
    ).fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO departments VALUES (?,?,?)", DEPARTMENTS
        )
        cursor.executemany(
            "INSERT INTO students VALUES (?,?,?,?,?)", STUDENTS
        )
        cursor.executemany(
            "INSERT INTO courses VALUES (?,?,?,?)", COURSES
        )
        cursor.executemany(
            "INSERT INTO enrollments VALUES (?,?,?,?,?)", ENROLLMENTS
        )
        cursor.executemany(
            "INSERT INTO professors VALUES (?,?,?,?)", PROFESSORS
        )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_university_db()
    print(f"University database created at {UNIVERSITY_DB_PATH}")

    conn = sqlite3.connect(UNIVERSITY_DB_PATH)
    for table in [
        "departments",
        "students",
        "courses",
        "enrollments",
        "professors",
    ]:
        count = conn.execute(
            f"SELECT COUNT(*) FROM {table}"
        ).fetchone()[0]
        print(f"   {table}: {count} rows")
    conn.close()