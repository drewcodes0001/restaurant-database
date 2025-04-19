import mysql.connector
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS

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
    print("Connected to Amazon RDS successfully")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

#flask instance
app = Flask(__name__)
CORS(app)

config = {
    'host' : endpoint,
    'user' : username,
    'password' : key, 
    'database' : 'restaurant_database'
    
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
    full_name = data.get('fullname')
    wage = data.get('wage')
    
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees (employee_id, username, password, full_name, wage) VALUES "
        "(%s, %s, %s, %s, %s)",
        (id, username, password, full_name, wage)
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
    cursor.execute("DELETE FROM employees WHERE employee_id = (%s)", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Employee removed successfully"}), 200

@app.route('/add_shift', methods=['POST'])
def add_shift():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    shift_id = data.get('shift_id')
    shift_date = data.get('shift_date')
    duration = data.get('duration')
    
    
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO shifts (shift_id, shift_date, duration) VALUES (%s, %s, %s)",
        (shift_id, shift_date, duration)
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
    cursor.execute("DELETE FROM shifts WHERE shift_id = (%s)", (shift_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Shift removed successfully"}), 200


def add_ingredient_to_stock():
    data = request.get_json() 
    if not data:
        return jsonify({"error": "No data provided"}), 400
      
    ingredient_id = data.get('ing_id')
    name = data.get('name')
    shelf_life = data.get('shelf_life')
    
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ingredients (ingredient_id, name, shelf_life) VALUES (%s, %s, %s)", 
                   (ingredient_id, name, shelf_life))
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
    cursor.execute("INSERT INTO dishes (dish_id, price, name) VALUES (%s, %s, %s)", (dish_id,price,name))
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
    cursor.execute("INSERT INTO dish_ingredients(dish_id,ingredient_id) VALUES (SELECT dish_id FROM dishes WHERE name=%s, SELECT ingredient_id FROM ingreidents WHERE name=%s)", (dish_name,ing_name))
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
      
    order_id = data.get('order_id')
    dish_name = data.get('dish_name')
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Order_Dishes(order_id,dish_id) VALUES (%s,SELECT dish_id FROM Dish WHERE name=%s)", (order_id,dish_name))
    conn.commit()
    conn.close()
    return jsonify({"message": "Dish added to order successfully"}), 200

def view_orders():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Order")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    conn.close()
    return jsonify({"message": ""}), 200

def view_dishes():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Dishes")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    conn.close()
    return jsonify({"message": ""}), 200

def view_menu():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Dishes")
    for (name,price) in cursor:
        print("Name: {}, Price: {}".format(
            name, price))
    conn.close()
    return jsonify({"message": ""}), 200

def view_ingredients():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Ingredients")
    
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    conn.close()
    return jsonify({"message": ""}), 200
    
    
    
    
#Statistics


#Employee


def count_employees():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Employees")
    (result,) = cursor.fetchone()
    print(f"Number of Employees = {result}")
    conn.close()
    return jsonify({"employee_count": result}), 200

def avg_salary():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(wage) FROM Employees")
    (result,) = cursor.fetchone()
    print(f"Average Wage of Employees = {result}")
    conn.close()
    return jsonify({"avg_salary": result}), 200

def max_salary():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(wage) FROM Employees")
    (result,) = cursor.fetchone()
    print(f"Max Salary = {result}")
    conn.close()
    return jsonify({"max_salary": result}), 200

def min_salary():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT MIN(wage) FROM Employees")
    (result,) = cursor.fetchone()
    print(f"Min Salary = {result}")
    conn.close()
    return jsonify({"min_salary": result}), 200


def sum_salary():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(wage) FROM Employees")
    (result,) = cursor.fetchone()
    print(f"Sum of Wages = {result}")
    conn.close()
    return jsonify({"sum_wages": result}), 200


#Customer

def count_customers():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Customers")
    (result,) = cursor.fetchone()
    print(f"Number of Customers = {result}")
    conn.close()
    return jsonify({"customer_count": result}), 200

def avg_points():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(reward_points) FROM Customers")
    (result,) = cursor.fetchone()
    print(f"Average Points of Customers = {result}")
    conn.close()
    return jsonify({"avg_points": result}), 200

def max_points():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(reward_points) FROM Customers")
    (result,) = cursor.fetchone()
    print(f"Max Points = {result}")
    conn.close()
    return jsonify({"max_points": result}), 200

def min_points():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT MIN(reward_points) FROM Customers")
    (result,) = cursor.fetchone()
    print(f"Min Points = {result}")
    conn.close()
    return jsonify({"min_points": result}), 200

def reward_eligible_customers():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Customers WHERE reward_point>50")
    (result,) = cursor.fetchone()
    print(f"Reward Eligible Customers = {result}")
    conn.close()
    return jsonify({"reward_eligible_customers": result}), 200
    
    
    

#Orders


def count_preparing_orders():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Customer_orders WHERE status LIKE Preparing")
    (result,) = cursor.fetchone()
    print(f"Preparing Orders = {result}")
    conn.close()
    return jsonify({"preparing_orders": result}), 200


def count_ready_orders():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Customer_orders WHERE status LIKE Ready")
    (result,) = cursor.fetchone()
    print(f"Ready Orders = {result}")
    conn.close()
    return jsonify({"ready_orders": result}), 200

def count_received_orders():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Customer_orders WHERE status LIKE Received")
    (result,) = cursor.fetchone()
    print(f"Received Orders = {result}")
    conn.close()
    return jsonify({"received_orders": result}), 200

def count_canceled_orders():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Customer_orders WHERE status LIKE Canceled")
    (result,) = cursor.fetchone()
    print(f"Canceled Orders = {result}")
    conn.close()
    return jsonify({"canceled_orders": result}), 200

def count_noncanceled_orders():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Customer_orders WHERE status <> Canceled")
    (result,) = cursor.fetchone()
    print(f"Noncanceled Orders = {result}")
    conn.close()
    return jsonify({"noncanceled_orders": result}), 200

def avg_price_orders():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(total_price) FROM Customer_orders")
    (result,) = cursor.fetchone()
    print(f"Average Order Price = {result}")
    conn.close()
    return jsonify({"avg_price_orders": result}), 200


#Dishes

def count_dishes():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Dishes")
    (result,) = cursor.fetchone()
    print(f"Number of Dishes = {result}")
    conn.close()
    return jsonify({"count_dishes": result}), 200

def avg_price_dishes():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(price) FROM Dishes")
    (result,) = cursor.fetchone()
    print(f"Average Dish Price = {result}")
    conn.close()
    return jsonify({"average_dish_price": result}), 200

def min_price_dishes():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT MIN(price) FROM Dishes")
    (result,) = cursor.fetchone()
    print(f"Min Dish Price = {result}")
    conn.close()
    return jsonify({"min_dish_price": result}), 200

def max_price_dishes():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(price) FROM Dishes")
    (result,) = cursor.fetchone()
    print(f"Max Dish Price = {result}")
    conn.close()
    return jsonify({"max_dish_price": result}), 200


#Ingredients

def count_ingredients():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Ingredients")
    (result,) = cursor.fetchone()
    print(f"Number of Ingredients = {result}")
    conn.close()
    return jsonify({"count_ingredients": result}), 200

def min_shelf_life_ingredients():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT MIN(shelf_life) FROM Ingredients")
    (result,) = cursor.fetchone()
    print(f"Min Shelf Life of Ingredients = {result}")
    conn.close()
    return jsonify({"min_shelf_life_ingredients": result}), 200

def max_shelf_life_ingredients():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(shelf_life) FROM Ingredients")
    (result,) = cursor.fetchone()
    print(f"Max Shelf Life of Ingredients = {result}")
    conn.close()
    return jsonify({"max_shelf_life_ingredients": result}), 200