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
user_id=1
name="Julia Jones"
library_num=1
def add_workout_session(id,name,library_id):
        cursor=conn.cursor()
        query=" INSERT INTO members(id, name,library_id) VALUES (%s, %s, %s)"
     
        cursor.execute(query,(user_id,name,library_num))
        if conn and conn.is_connected():
            print(f" New session added for member {name}")
            pass
        cursor.close()
        conn.close()
        conn.commit()
try:
  ValueError
except Error as e:
  print("There seems to be an error")
    
finally:
     print (f" New session added for member {name}") 
