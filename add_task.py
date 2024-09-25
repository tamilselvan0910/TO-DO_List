#!/usr/bin/env python3

import cgi
import mysql.connector

# Get form data
form = cgi.FieldStorage()
task_content = form.getvalue("task")

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="todo_db"
)

cursor = db.cursor()
cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task_content,))
db.commit()
cursor.close()

# Redirect back to the main page (index.html)
print("Location: /index.html")
print()  # This is necessary to end the headers.
