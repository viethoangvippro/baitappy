import pandas as pd
import mysql.connector
import pandas as pd
import mysql.connector
import xlrd
from mysql.connector import MySQLConnection, Error

myconn = mysql.connector.connect(host = "localhost", user = "root",
passwd = "", database = "database")

cur = myconn.cursor()



# # THEM
# sql = ("insert into students(id, code, first_name, last_name, birthOfDate, math, physics, chemistry) "
# + "values (%s, %s, %s, %s, %s, %s, %s, %s)")

# # giá trị của một row được cung cấp dưới dạng tuple
# val = (53, "c200454", "Hoang", "dep try", "18/5/2002",2.22,2.25,2.66)

# try:
# #inserting the values into the table
#     cur.execute(sql,val)
# #commit the transaction
#     myconn.commit()
# except:
#     myconn.rollback()
#     print(cur.rowcount,"record inserted!")
#     myconn.close()


#SUA
# try:
#     # cập nhật name cho bảng students
#     cur.execute("update students set first_name = 'Đạt' where id = 53")
#     myconn.commit()
# except:
#     myconn.rollback()
#     myconn.close()

#XOA
# try:
# # cập nhật name cho bảng students
#     cur.execute("delete from students where id = 53")
#     myconn.commit()
# except:
#     myconn.rollback()
#     myconn.close()


cur.execute("SELECT * FROM students")

myresult = cur.fetchall()

for x in myresult:
  print(x)



# df = pd.read_excel('G:\\pythontl\\task02\\input.xlsx', sheet_name='MAU', usecols='A:H', skiprows=10, nrows=52)
# data = []
# for row in df.iterrows():
#     row_data = []
#     for value in row[1]:
#         row_data.append(value)
#     sql = "insert into students(id, code, first_name, last_name, birthOfDate, math, physics, chemistry) values (%s,%s,%s,%s,%s,%s,%s,%s)"
#     conn = connect()
#     val = (row_data[0],row_data[1],row_data[2],row_data[3],row_data[4],row_data[5],row_data[6],row_data[7])
#     cursor = conn.cursor()
#     cursor.execute(sql, val)
#     conn.commit()
#     data.append(row_data)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="database"
# )

# cur = mydb.cursor()

# loc = ('G:\\pythontl\\task02\\input.xlsx')

# a=xlrd.open_workbook(loc)

# sheet = a.sheet_by_index(0)
# sheet.cell_value(0,0)
# for i in range(11,63):
#     print(sheet.row_value(i))
# mydb.close()


# cur.execute("create table student(id int primary key, name varchar(100),date varchar(100), toan double, ly double, hoa double)")

# mydb.close()




# df = pd.read_excel('G:\\pythontl\\task02\\input.xlsx', sheet_name='MAU', usecols='A:H', skiprows=10, nrows=52)

# data = []

# for row in df.iterrows():
#     row_data = []
#     for value in row[1]:
#         row_data.append(value)
#     data.append(row_data)

# print(data)



# file_name = 'G:\\pythontl\\task02\\input.xlsx' 
# df = pd.read_excel(file_name, skiprows=9, nrows=52)
# print(df)



# def connect():
#     db_config = {
#         'host': 'localhost',
#         'database': 'database',
#         'user': 'root',
#         'password': ''
#     }
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
#     conn = None
 
#     try:
#         conn = MySQLConnection(**db_config)
 
#         if conn.is_connected():
#             return conn
 
#     except Error as error:
#         print(error)
 
#     return conn