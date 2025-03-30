import mysql.connector
import os
from dotenv import load_dotenv

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
