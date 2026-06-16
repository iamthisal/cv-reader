import sqlite3
import json

from websockets.frames import DATA_OPCODES

DB_NAME = "cv_data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    
    CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    skills TEXT,
    experience TEXT,
    education TEXT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    
    """)

    conn.commit()
    conn.close()

def save_candidate(data: dict):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    
    INSERT INTO candidates (name,email,skills,experience, education)
    VALUES (?, ?, ?, ?,?)
    
    """,(
        data.get("name"),
        data.get("email"),
        json.dumps(data.get("skills", [])),
        json.dumps(data.get("experience",[])),
        data.get("education")
    ))
    conn.commit()
    conn.close()


def get_all_candidates():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM candidates ORDER BY uploaded_at DESC")
    rows = cursor.fetchall()
    conn.close()

    candidates = []

    for row in rows:
        candidates.append({
            "id" : row[0],
            "name" : row[1],
            "email" : row[2],
            "skills": json.loads(row[3]),
            "experience" : json.loads(row[4]),
            "education" : row[5],
            "uploaded_at" : row[6]
            })

    return candidates
