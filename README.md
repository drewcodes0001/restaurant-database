# restaurant-database
## Setting up the DBMS connection
---
You might have to do `pip install mysql-connector-python` if you run into an error `ModuleNotFoundError: No module named 'mysql'`

Setting up the key variable to hold your MySQL password
1. Create a `.env` file and store the password there: `MYSQL_PASSWORD=yourpassword`
    - You might have to do `pip install python-dotenv`
2. The `.gitignore` file should exlude the .env file from commits


To run the add data website, try running the python script, then use `flask run`