import mysql.connector
myDb = mysql.connector.connect(
    host="127.0.0.1", user="root", passwd="Sam1524", database="sql_clothing")

myCursor = myDb.cursor()
#selectCommand = "CREATE TABLE sql_customers (customerId int AUTO_INCREMENT PRIMARY KEY, fullName VARCHAR(255), address text, number int, prime int)"
#selectCommand = "CREATE TABLE sql_store (storeId int, name text, address text, invId int, locationCode int)"
#selectCommand = "CREATE TABLE sql_inventory (prodId int, fullName text, description text, qty int, price int, locId int)"
#selectCommand = "CREATE TABLE sql_location (locId int, name text)"
#myCursor.execute(selectCommand)
#myCursor.execute(selectCommand)
#myCursor.execute(selectCommand)
#myCursor.execute(selectCommand)
#result = myCursor.fetchall()
#for row in result:
    #print(f"{row[0]} {row[1]}")

myDb.commit()
myDb.close()
