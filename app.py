import mariadb
import dbcreds

def blogger():
    username = input("Please provide a username: ")
    dob = input("Please provide your date of birth (yyyy-mm-dd): ")
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    print(result)

    cursor = conn.cursor