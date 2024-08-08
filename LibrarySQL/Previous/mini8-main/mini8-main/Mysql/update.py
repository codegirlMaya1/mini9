import mysql.connector
from mysql.connector import Error



user="root"
password="S05071984"
host="127.0.0.1"
db_name="admin_db"


try:
    conn=mysql.connector.connect(
    database=db_name,
    user=user,
    password=password,
    host=host
    
)
    update_title=("HATCHETT",1)
    update_id=("5",1)
    
    #Assuming Bob Green has an id of 2
    def update_member_age(member_id, new_age):
        cursor=conn.cursor()
        query="UPDATE members SET title = %s WHERE %s"
        query1="UPDATE members SET id = %s WHERE %s"
        cursor.execute(query,update_title)
        cursor.execute(query1,update_id)
        
        if conn and conn.is_connected():
            print("Member data updated successfully")
            pass
            cursor.close()
            conn.close()
    conn.commit()
except Error as e:
    print("There seems to be an error")
    
finally:
     print (" Member data updated successfully") 