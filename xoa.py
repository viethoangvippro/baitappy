import pandas as pd
import mysql.connector
import pandas as pd
import mysql.connector
import xlrd
from mysql.connector import MySQLConnection, Error

myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "", database = "database")

cur = myconn.cursor()


def xoaStudent() :
    #XOA
    try:
    # cập nhật name cho bảng students
        cur.execute("delete from students where id = 53")
        myconn.commit()
    except:
        myconn.rollback()
        myconn.close()
print ()
