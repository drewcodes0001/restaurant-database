import mysql.connector
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for


load_dotenv()
key = os.getenv("MYSQL_PASSWORD") # create a .env file with your MySQL password

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = key, 
    port = '3306',
    database = 'mydb' 
)

mycursor = mydb.cursor() 
mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)

#flask instance
app = Flask(__name__)

config = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : key, 
    'database' : 'mydb'
    
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add',methods=['POST'])
def add():
    id = request.form['id']
    username = request.form['username']
    password = request.form['password']
    fullname = request.form['fullname']
    wage = request.form['wage']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employee (employee_id,username, password, Full_name, wage) VALUES (%s,%s, %s, %s, %s)", (id,username, password, fullname, wage))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete',methods=['POST'])
def delete():
    id = request.form['id_remove']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employee WHERE employee_id = (%s)",(id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))