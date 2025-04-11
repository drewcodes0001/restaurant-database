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

mycursor.close();

