import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="0000", database="alx_book_store"
)


mycursor = mydb.cursor()

mycursor.execute(
    """
CREATE DATABASE IF NOT EXISTS alx_book_store (
  id INT  PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255)
)
"""
)

print("Table created successfully!")

mycursor.close()
mydb.close()
