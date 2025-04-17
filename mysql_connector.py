import mysql.connector
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS




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
CORS(app)

config = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : key, 
    'database' : 'mydb'
    
}

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()  # Receive JSON data
    if not data:
        return jsonify({"error": "No data provided"}), 400
      
    id = data.get('id')
    username = data.get('username')
    password = data.get('password')
    fullname = data.get('fullname')
    wage = data.get('wage')
    
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employee (employee_id, username, password, Full_name, wage) VALUES (%s, %s, %s, %s, %s)",
        (id, username, password, fullname, wage)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Employee added successfully"}), 200

@app.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()  # Receive JSON data
    if not data:
        return jsonify({"error": "No data provided"}), 400
      
    id = data.get('id_remove')
    
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employee WHERE employee_id = (%s)", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Employee removed successfully"}), 200

@app.route('/add_shift', methods=['POST'])
def add_shift():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    shift_id = data.get('shift_id')
    date = data.get('date')
    duration = data.get('duration')
    
    
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Shift (Shift_id, Date, Duration) VALUES (%s, %s, %s)",
        (shift_id, date, duration)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Shift added successfully"}), 200
    
@app.route('/delete_shift', methods=['POST'])
def delete_shift():
    data = request.get_json()  # Receive JSON data
    if not data:
        return jsonify({"error": "No data provided"}), 400
      
    shift_id = data.get('id_remove_shift')
    
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Shift WHERE Shift_ID = (%s)", (shift_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Shift removed successfully"}), 200


def add_ingredient_to_menu():
    data = request.get_json() 
    if not data:
        return jsonify({"error": "No data provided"}), 400
      
    ing_id = data.get('ing_id')
    name = data.get('name')
    shelf_life = data.get('shelf_life')
    
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Ingredient (ing_id, name, shelf_life) VALUES (%s, %s, %s)", (ing_id,name,shelf_life))
    conn.commit()
    conn.close()
    return jsonify({"message": "Ingredient added to menu successfully"}), 200

def add_dish_to_menu():
    data = request.get_json() 
    if not data:
        return jsonify({"error": "No data provided"}), 400
      
    dish_id = data.get('dish_id')
    name = data.get('name')
    price = data.get('price')
    
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Dish (dish_id, price, name) VALUES (%s, %s, %s)", (dish_id,price,name))
    conn.commit()
    conn.close()
    return jsonify({"message": "Dish added to menu successfully"}), 200


def add_ingredient_to_dish():
    data = request.get_json() 
    if not data:
        return jsonify({"error": "No data provided"}), 400
      
    dish_name = data.get('dish_name')
    ing_name = data.get('ing_name')
    
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Dish_ingredient(d_id,i_id) VALUES (SELECT dish_id FROM Dish WHERE name=%s, SELECT ing_id FROM Ingreident WHERE name=%s)", (dish_name,ing_name))
    conn.commit()
    conn.close()
    return jsonify({"message": "Dish added to menu successfully"}), 200


def add_dish_to_order():
    data = request.get_json() 
    if not data:
        return jsonify({"error": "No data provided"}), 400
      
    dish_name = data.get('dish_name')
    order_id = data.get('order_id')
    
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Order_Dish(o_id,d_id) VALUES (%s,SELECT dish_id FROM Dish WHERE name=%s)", (order_id,dish_name))
    conn.commit()
    conn.close()
    return jsonify({"message": "Dish added to order successfully"}), 200


def calculate_order_price():
    data = request.get_json() 
    if not data:
        return jsonify({"error": "No data provided"}), 400
      
    dish_name = data.get('order_id')
    
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Order_Dish(o_id,d_id) VALUES (%s,SELECT dish_id FROM Dish WHERE name=%s)", (order_id,dish_name))
    conn.commit()
    conn.close()
    return jsonify({"message": "Dish added to order successfully"}), 200

def view_orders():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Order")
    for (order_id, status, total_price, emp_id,cust_id) in cursor:
        print("Order id: {}, Status: {}, Total Price: {}, Employee id: {}, Customer id:{} ".format(
            order_id, status, total_price, emp_id,cust_id))
    conn.close()
    return jsonify({"message": ""}), 200
    