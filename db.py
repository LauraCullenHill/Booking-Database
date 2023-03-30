import mysql.connector

def get_my_sql_connection():
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        user="LauraCullen",
        password="Hector2021-",
        auth_plugin='mysql_native_password',
        database="nano"
    )