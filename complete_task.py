#!/usr/bin/env python3

import cgi
import mysql.connector

# Get task ID
form = cgi.FieldStorage()
task_id = form.getvalue("id")

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="todo_db"
)

cursor = db.cursor()
cursor.execute("UPDATE tasks SET status = TRUE WHERE id = %s", (task_id,))
db.commit()
cursor.close()

# Redirect back to the task list
print("Location: /cgi-bin/get_tasks.py\n")
