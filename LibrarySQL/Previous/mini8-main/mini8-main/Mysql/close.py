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
try:
    def new_user(id, name, biography):
        cursor=conn.cursor()
        new_member=("5", "Sally Smith", "6")
        query=" INSERT INTO users(id, name, biography) VALUES (%s, %s, %s)"
        cursor.execute(query,new_member)
        conn.commit()
        ab1=cursor
        print("New member added successfully")
        
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("New member Sally added successfully")
except Error as e:
    
    print("There seems to be an error")
finally:
     print ("Connection now closed. Thank you")