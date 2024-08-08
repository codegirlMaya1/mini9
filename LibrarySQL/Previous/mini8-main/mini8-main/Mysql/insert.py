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
    jane_doe_id=3
    book_name= "Babysitter Club"
    aut_id=22
    ind_book="Ys4123"
    new_date="2024-01-15"
    c_stat= "Available"
    def add_book(id, title,author_id,isbn, publication_date, availability):
        cursor=conn.cursor()
        query=" INSERT INTO books(id, title,author_id,isbn, publication_date, availability) VALUES (%s, %s, %s, %s,%s, %s)"
     
        cursor.execute(query,(jane_doe_id,book_name,aut_id,ind_book,new_date,c_stat))
       
        
        if conn and conn.is_connected():
            print(f" New book title added: {book_name}")
            pass
            cursor.close()
            conn.close()
    conn.commit()
except Error as e:
    print("There seems to be an error")
    
finally:
     print (f" New book title added: {book_name}") 
