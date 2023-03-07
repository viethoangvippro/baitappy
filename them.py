import pandas as pd
import mysql.connector
import pandas as pd
import mysql.connector
import xlrd
from mysql.connector import MySQLConnection, Error

myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "", database = "database")

cur = myconn.cursor()

def themStudent() :
    # THEM
    sql = ("insert into students(id, code, first_name, last_name, birthOfDate, math, physics, chemistry) "
    + "values (%s, %s, %s, %s, %s, %s, %s, %s)")
    # giá trị của một row được cung cấp dưới dạng tuple
    val = (53, "c200454", "Hoang", "dep try", "18/5/2002",2.22,2.25,2.66)
    try:
        #inserting the values into the table
        cur.execute(sql,val)
        #commit the transaction
        myconn.commit()
    except:
        myconn.rollback()
    print(cur.rowcount,"record inserted!")
    myconn.close()
print ()






