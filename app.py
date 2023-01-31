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

def login():
    username = input("Please provide a username: ")
    password = input("Please provide a password: ")
    logged_in = "SELECT id FROM client WHERE username (?,?)"
    cursor.execute(logged_in, (username, password))
    results = cursor.fetchone()
    if results is True:
        id = results[0]
        print(id)
    else:
        print("Incorrect Username and/or Password")

def prompt():
    print("Welcome to BLOGGER!\
        \nPlease select from the following:\
        \n1. Make a new post\
        \n2. See all posts\
        \n3. Exit")
    selection = input("Please enter your selection: ")
    return selection

def blogger():
    cursor.execute("SELECT * FROM client")
    result = cursor.fetchall()
    print(result)

def client_post(client_id):
    title = input("Title: ")
    content = input("Post: ")
    make_post = "SELECT id FROM client WHERE username (?,?,?)"
    cursor.execute(make_post, (client_id, title, content))

def posts():
    cursor.execute("SELECT * FROM posts")
    result = cursor.fetchall()
    for post in result:
        print(post)

def choice():
    login()
    print("Welcome to the application!")
    while True:
        try:
            selection = int(prompt())
        except ValueError:
            print("Please enter numbers only")
            continue
        if selection == 1:
            client_post()
        elif selection == 2:
            posts()
        elif selection == 3:
            print("Goodbye")
            break
        else:
            print("Your input is invalid! Please select from the displayed options.")