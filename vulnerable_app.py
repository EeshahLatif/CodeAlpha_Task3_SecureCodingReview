import os
import sqlite3

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # ❌ SQL Injection risk
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        print("Login successful!")
    else:
        print("Login failed!")

def run_command():
    cmd = input("Enter system command: ")
    # ❌ Command Injection risk
    os.system(cmd)

# Example run
login("admin", "1234")
run_command()
