import mysql.connector as mc
from mysql.connector import errorcode as ec

user = "retail_user"
password = "venkatramasai"
host = "34.72.140.44"
db = "retail_db"

connection = mc.connect(user=user,
                        password=password,
                        host=host,
                        database=db
                        )

orders_cursor = connection.cursor()
query = """SELECT * FROM orders LIMIT 10"""
orders_cursor.execute(query)

for order in orders_cursor:
    print(order)
