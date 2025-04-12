import mysql.connector
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for


load_dotenv()
endpoint = os.getenv("ENDPOINT") 
username = os.getenv("USERNAME")
key = os.getenv("MYSQL_PASSWORD")

try:
    mydb = mysql.connector.connect(
        host=endpoint,
        user=username,
        password=key,
        port='3306',
        database='restaurant_database'
    )
    print("Connected to RDS!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

mycursor = mydb.cursor() 
mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)

mycursor.close()

@app.route('/add', methods=['POST'])
def add():
    id = request.form['id']
    username = request.form['username']
    password = request.form['password']
    fullname = request.form['fullname']
    wage = request.form['wage']
    # Optional: handle missing start_date and supervisor_username
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO employees (employee_id, username, password, full_name, wage)
        VALUES (%s, %s, %s, %s, %s)
    """, (id, username, password, fullname, wage))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    id = request.form['id_remove']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE employee_id = %s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

