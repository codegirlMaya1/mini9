import mysql.connector
from mysql.connector import Error



user="root"
password="S05071984"
host="127.0.0.1"
db_name="admin_db"

conn=mysql.connector.connect(
    database=db_name,
    user=user,
    password=password,
    host=host
    
)

