import mysql.connector
mydb = mysql.connector.connect (
    host='localhost',
    user='root',
    password=''
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("USE sales") 
mycursor.execute("SELECT * FROM customer")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

mycity = ['']
mycity[0] = input("\nCity to search: ")
myquery = 'SELECT * FROM customer WHERE city = %s'
mycursor.execute(myquery, mycity)
myresult = mycursor.fetchall()
for x in myresult: print(x)
print(mycursor.rowcount, "rows")
myid = ['']
myid[0] = input("\nId of the customer to delete: ")
myquery = "DELETE FROM customer WHERE idcustomer = %s"
mycursor.execute(myquery, myid)
if mycursor.rowcount == 0:
    print("Customer", myid[0], "NOT FOUND" )
else:
    print("Customer", myid[0], "DELETED")
mycursor.execute("COMMIT")
mydb.close()