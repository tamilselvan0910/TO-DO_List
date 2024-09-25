#!/usr/bin/env python3

import mysql.connector
import json

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="todo_db"
)

cursor = db.cursor(dictionary=True)
cursor.execute("SELECT * FROM tasks ORDER BY id DESC")
tasks = cursor.fetchall()
cursor.close()

# Output the tasks as HTML
print("Content-Type: text/html\n")
print("<html><head><title>To-Do List</title></head><body>")
print("<h1>To-Do List</h1>")
print("<ul>")
for task in tasks:
    print(f"<li>{task['task']} {'(Completed)' if task['status'] else ''}")
    if not task['status']:
        print(f"<a href='/cgi-bin/complete_task.py?id={task['id']}'>Mark Complete</a>")
    print(f"<a href='/cgi-bin/delete_task.py?id={task['id']}'>Delete</a></li>")
print("</ul>")
print("</body></html>")
