import os
import psycopg2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

DATABASE_URL = os.environ["DATABASE_URL"]


def get_conn():
    return psycopg2.connect(DATABASE_URL)


@app.on_event("startup")
def startup():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()


class UserCredentials(BaseModel):
    username: str
    password: str


@app.post("/register")
def register(creds: UserCredentials):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (creds.username, creds.password),
        )
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "User created"}
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=400, detail="Username already exists")


@app.post("/login")
def login(creds: UserCredentials):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id FROM users WHERE username = %s AND password = %s",
        (creds.username, creds.password),
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    return {"success": row is not None}
