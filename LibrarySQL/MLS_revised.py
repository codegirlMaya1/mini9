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
    conn=mysql.connector.connect(
        user=user,
        password=password,
        host=host
    
)
    if conn.is_connected():
        print("Thank you for entering the libraries BOOK MySQL admin database")
        mycursor = conn.cursor()
        
            
   
except ValueError as e:
    print(f'Error: {e}')
 
finally:
    if conn and conn.is_connected():
       
        print(" Your libraries MySQL  admin database is open...")
        
        


main_menu="""
Welcome to the Library Management System!

    Main Menu:
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Genre Operations
    5. Quit


"""

menu1 = """
Book Operations:
        1. Add a new book
        2. Borrow a book
        3. Return a book
        4. Search for a book
        5. Display all books
        6. Pay Book Fines
"""
menu2 = """
User Operations:
        1. Add a new user
        2. View user details
        3. Display all users
"""
menu3 = """
Author Operations:
        1. Add a new author
        2. View author details
        3. Display all authors
"""
menu4 = """
Genre Operations:
        1. Add a new genre
        2. View genre details
        3. Display all genres
"""



genre_details="""
 This section was implemented to help users create categories
 that show similiar writing styles, topics, ect to help other users 
 searching for literature through this library....

"""

user_details="""
This section was implemented to help users enter unique details about
their interest to help assist online group creators contact compatible users
about upcoming events, ect...
"""
author_details="""
This section helps users learn new exciting, interesting and fun facts 
about their favor authors.
"""

import os

user = []
user1 = []
user1_id = []
library1_id = []
author1=[]
genre1=[]
user_cost=10
user_cost1=15
user_cost2=20


class User:
    def __init__(self,user):
        self.user=user
        
def add_user():
 
        new_user = input("Enter user name:")
        get_user=(new_user)
        user1.append(get_user)
        print("You have successfully added a new user.")
        new_user_id = input("Enter user id:")
        get_user_id=(new_user_id)
        user1_id.append(get_user_id)
        print("You have successfully added your user id.")
        new_library_id = input("Enter library id:")
        get_library_id=(new_library_id)
        library1_id.append(get_library_id)
        print("You have successfully added your library id.")
        
            
    
       
def user_fines():
   while True:
    user_fines1=int(input("How many days was the members book late?"))
    if user_fines1<= 5:
        print(f"You owe {user_cost}")
        payment=int(input("Enter the amount the member has paid: "))
    if payment != user_cost:
        print(" Please collect the total amount from the member. Now exiting the database. Please refresh")
    elif payment==user_cost:
        print("The members payment was accepted through admin. Please notify the member new books are available")
        main_menu1()
    elif user_fines1>=5:
        print(f"You owe {user_cost2}")
        payment=int(input(" Enter the payment amount: "))
    if payment != user_cost2:
        print(" The member has not satisfied the library fine please exit the payment system")
    elif payment==user_cost2:
        print("Thanks for your payment")
        main_menu1()
    

           
           
def display_user():
    if len(user1) >= 1:
        print(" showing...")
        main_menu1()
    else:
        print(f"New user{user} User Id:{user1_id} Library id ={library1_id}")

def user_details():
    print(user1)

def user_menu():
    while True:
        print(menu2)
        user_select=input("Enter your selection: ")
        while True:
            if user_select=="1":
                add_user()
                print("Make a selection")
                user_select=input("Enter your selection: ")
           
            elif user_select=="2":
                user_details()
                user_select=input("Enter your selection: ")
            elif user_select=="3":
                display_user()
            else:
                print( "User made an invalid selection not = to 1, 2, 3, System error please try again")
def main_menu1():
    print("*** MENU ***")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Genre Operations")
    print("5. Quit")
    
    ch = int(input("Enter your choice: "))
    if ch == 1:
      book_operations()
    elif ch==2:
        user_menu()
    elif ch==3:
        author_menu()
    elif ch==4:
        genre_menu()
     
    elif ch == 5:
        print("You have finished. Thank you. Goodbye!")
       
    else:
        print("You entered a wrong number. Please try again.")
        input("Press Enter to continue...")  # Adding pause before clearing the screen again
        os.system("cls" if os.name == "nt" else "clear")  # Clearing the screen


class genre:
    def __init__(self,genre):
        self.genre=genre
def add_genre():
    new_genre = input("Enter the genre you would like to add:")
    get_genre=(new_genre)
    genre1.append(get_genre) if get_genre not in genre1 else print("You have successfully added a new genre.")
  

def display_genre():
    print(f" Now displaying current genres in this section: {genre1}")
    main_menu1()
   
    
def genre_details():
    print(genre1)

def genre_menu():
    print(menu4)
    genre_select=input("Enter your selection: ")
    while True:
        if genre_select=="1":
            add_genre()
            print("Make a selection")
            genre_select=input("Enter your selection: ")
           
            
        elif genre_select=="2":
            genre_details()
            genre_select=input("Enter your selection: ")
        elif genre_select=="3":
            display_genre()
            genre_select=input("Enter your selection: ")
        else:
            print("Input not = to 1, 2, or 3. PlEASE START OVER....")
class Author:
    def __init__(self,author):
        self.author=author
def add_author():
    new_author = input("Enter the authors last name:")
    get_author=(new_author)
    author1.append(get_author)
    print("You have successfully added a new author.")
    pass

def display_author():
    print(f"Authors listed: {author1}" )
    main_menu1()
    

def author_details():
    print(author1)

def author_menu():
    print(menu3)
    author_select=input("Enter your selection: ")
    while True:
        if author_select=="1":
            add_author()
            print("Make a selection")
            author_select=input("Enter your selection: ")
           
            
        elif author_select=="2":
            author_details()
        elif author_select=="3":
            display_author()
            main_menu1()
            
        else:   
            print(" Input not = to 1, 2, or 3. PlEASE START OVER....")
            menu_choice6=input("Make a selection: ")
            print(main_menu)
            if menu_choice6=="1":
                print(menu1)
                book_menu
            elif menu_choice6=="2":
                print(menu2)
                user_menu
            elif menu_choice6=="3":
                print(menu3)
                author_menu
            elif menu_choice6=="4":
                print(menu4)
                genre_menu


        
class Book:
    def __init__(self,book):
        self.book=book
def add_book():
    name = input("Enter the book name you want to add: ")
    outer_name = input("Enter the author name: ")
    book_id = int(input("Enter the ID of the book: "))
    shelf = input("Enter the position of the book on the shelf: ")
    status = input("Enter the status (borrowed or in library): ")
    users = {"name": name, "outer_name": outer_name, "book_id": book_id, "shelf": shelf, "status": status}
    user.append(users)
    print("You have successfully added the book.")
    book_cursor=conn.cursor()
    book_query="INSERT INTO add_book(Title, Author, ID, Shelf_Location, Book_Location) VALUES (%s,%s,%s,%s,%s)"
    book_value=("Cat in the Hat", "Dr. Suess"," 33", "12"," In library")
    book_cursor.execute(book_query,book_value)

    display_cursor=conn.cursor()
    display_query="INSERT INTO display_book(Title, Author, ID, Shelf_Location, Book_Location) VALUES (%s,%s,%s,%s,%s)"
    display_value=("Cat in the Hat", "Dr. Suess"," 33", "12"," In library")
    display_cursor.execute(display_query,display_value)
    search_cursor=conn.cursor()
    search_query="INSERT INTO search_book(Title, Author, ID, Shelf_Location, Book_Location) VALUES (%s,%s,%s,%s,%s)"
    search_value=("Cat in the Hat", "Dr. Suess"," 33", "12"," In library")
    search_cursor.execute(search_query,search_value)

   

def return_book():
    name = input("Enter the book name you want to return: ")
    outer_name = input("Enter the author name: ")
    book_id = int(input("Enter the ID of the book (enter numbers only): "))
    shelf = input("Enter the position of the book on the shelf(enter numbers only): ")
    status = input("Enter the status (borrowed or return: ")
    users = {"name": name, "outer_name": outer_name, "book_id": book_id, "shelf": shelf, "status": status}
    user.append(users)
    return_cursor=conn.cursor()
    return_query="INSERT INTO return_book(Title, Author, ID, Shelf_Location, Book_Location) VALUES (%s,%s,%s,%s,%s)"
    return_value=("Cat in the Hat", "Dr. Suess"," 33", "12"," In library")
    return_cursor.execute(return_query,return_value)
    print("You have successfully returned the book.")
    other_info=input("Do you owe fines?: ")
    if other_info=="No":
        print(" Please proceed")
        main_menu1()
    elif other_info=="Yes":
        user_fines()


def display():
    if len(user) < 1:
        print("No books in the library.")
        main_menu1()

        
    else:
        print("The books in the library are:")
        for book in user:
            print(book)
            main_menu1()
        
def new_loop():
    menu_choice7=input(" Make a Selection: ")
    print(main_menu)
    if menu_choice7=="1":
        print(menu1)
        book_operations()
    elif menu_choice7=="2":
        print(menu2)
        user_menu()
    elif menu_choice7=="3":
        print(menu3)
        author_menu()
    elif menu_choice7=="4":
        print(menu4)
        genre_menu()
       


def search():
    ch = int(input("Enter the ID of the book you want to search for: "))
    found = False
    for i in user:
        if i["book_id"] == ch:
            print("Yes, the book is in the library.")
            found = True
            break
    if not found:
        print("Sorry, the book is not in the admin library.....Book also is not in stock? Please locate the book and provide system updates. Thank you....")

def edit():
    x = int(input("Enter the book ID you want to edit: "))
    for i in user:
        if i["book_id"] == x:
            s = input("Enter the new status: ")
            sh = input("Enter the new position of the book: ")
            i["shelf"] = sh
            i["status"] = s
            print("Your edit is successful.")
            print("The new book's data is", user)
            return
    print("Book not found.")

def remove():
    x = int(input("Enter the book ID you want to remove from the admin database: "))
    for i in user:
        if i["book_id"] == x:
            user.remove(i)
            print("Successfully removed.")
            print("The other books in the library are", user)
            return
    print("Book not found.")
    
def book_operations():
     while True:
          print(menu1)
          choice=input(" Make a selection: ")
          if choice=="1":
            add_book()
          elif choice=="2":
            remove()
          elif choice=="3":
            return_book()
          elif choice=="4":
           search()
          elif choice=="5":
            display()
          elif choice=="6":
              user_fines()
          else:
            print(user1)

def book_menu(): 
        print(menu1)
        menu_choice4=input(" Make a Selection: ")
        print(main_menu)
        if menu_choice4=="1":
             print(menu1)
             book_operations()
        elif menu_choice4=="2":
            print(menu2)
            user_menu
        elif menu_choice4=="3":
            print(menu3)
            author_menu
        elif menu_choice4=="4":
            print(menu4)
            genre_menu
    

print("-----------------------------------------------------------------------------")
print("                *** Welcome to the ADMIN library ***")
print("-----------------------------------------------------------------------------")
print("    Make a Selection Below:")
print("1. Alternative Menus are available in the database")
print("2.  Make a selection to display other menu options.")
print(".............................................................................")
while True:
   
    print("*** MENU ***")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Genre Operations")
    print("5. Quit")
    while True:
        ch = int(input("Enter your choice: "))
        if ch == 1:
            book_operations()
        elif ch==2:
            user_menu()
        elif ch==3:
            author_menu()
        elif ch==4:
            genre_menu()
        elif ch == 5:
            print("You have finished. Please log off the system. Thank you. Goodbye!")
            
        else:
            print("You entered a wrong number. Please try again...")
            input("Press Enter to continue...")  # Adding pause before clearing the screen again
            os.system("cls" if os.name == "nt" else "clear")  # Clearing the screen