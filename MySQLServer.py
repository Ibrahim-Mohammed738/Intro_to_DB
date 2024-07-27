import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="0000", database="alx_book_store"
)


mycursor = mydb.cursor()

mycursor.execute


mycursor.close()
mydb.close()
