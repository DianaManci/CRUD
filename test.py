import MySQLdb

try:
    connection =MySQLdb.connect(
        host="localhost",
        user="root",
        password="",
        db="flask"
    )

    print("conexion exitosa")
    connection.close()
except MySQLdb.Error as e:
    print(f"error:{e}")    