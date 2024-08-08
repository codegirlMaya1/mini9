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
id=1
try:    
    def user(id):
        if id ==1:
            cursor=conn.cursor()
            query="DELETE FROM user WHERE id = %s"
        
        cursor.execute(query,id)
        
        if conn and conn.is_connected():
            print(f"Member #{id} deleted successfully")
            pass
            cursor.close()
            conn.close()
            conn.commit()
except Error as e:
    print("Member was not deleted")
    
finally:
     print (f"Member #{id} deleted successfully") 