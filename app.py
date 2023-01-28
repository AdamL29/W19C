import mariadb
import dbcreds

conn = mariadb.connect(
    user = dbcreds.user,
    password = dbcreds.password,
    host = dbcreds.host,
    port = dbcreds.port,
    database = dbcreds.database
)
cursor = conn.cursor()

def prompt():
    print("Welcome to BLOGGER!\
        \nPlease select from the following:\
        \n1. Make a new post\
        \n2. See all posts\
        \n3. Exit")
    selection = input("Please enter your selection: ")
    return selection

def blogger():
    username = input("Please provide a username: ")
    password = input("Please provide a password: ")
    cursor.execute("SELECT * FROM client")
    result = cursor.fetchall()
    print(result)

def client(client_id):
    input("Title: ")
    input("Post: ")

def posts():
    cursor.execute("SELECT * FROM posts")
    result = cursor.fetchall()
    print(result)

def choice():
    print("Welcome to the application!")
    while True:
        try:
            selection = int(prompt())
        except ValueError:
            print("Please enter numbers only")
            continue
        if selection == 1:
            client()
        elif selection == 2:
            posts()
        elif selection == 3:
            print("Goodbye")
            break
        else:
            print("Your input is invalid! Please select from the displayed options.")