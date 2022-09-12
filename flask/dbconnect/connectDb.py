import mysql.connector
from numpy import insert

myDb = mysql.connector.connect(
    host="127.0.0.1",user="root", passwd="Sam1524",database="store")

myCursor = myDb.cursor()

#selectCommond ="SELECT first_name,last_name FROM orders o Join  customers c ON o.customer_id=c.customer_id"
#selectCommond ="CREATE TABLE appUsers (id int,username text, password text)"

#appUser=(1,"Akshay","abc")
appUsers =[(2,"Samhitha","c"),(3,"Abhi","b"),(4,"pratham","a")]
insertQuery ="Insert INTO appUsers VALUES(%s,%s,%s)"
myCursor.execute(insertQuery,appUsers)
#result =myCursor.fetchall()
#for row in result:
#    print(f"{row[0]} {row[1]}")

myDb.commit()
myDb.close()
