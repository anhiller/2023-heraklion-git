import json
import getpass

PATH = "./pwdb.json"

def get_credentials():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    return username, password

def read_pwdb():
    with open(PATH, "rt") as f:
        pwdb = json.load(f)
    return pwdb

def write_pwdb(pwdb):
    with open(PATH, "w") as f:
        json.dump(pwdb, f)


def authenticate(username, password, pwdb):
    if username in pwdb:
        if password == pwdb[username]:
            print("Successfully authenticated!")
        else:
            print("Wrong Password")
    else:
        while True:
            answer = input("Do you want to be added to the database? (y/n): ")
            if answer == "y":
                pwdb = add_user(username, password, pwdb)
                write_pwdb(pwdb)
                print("user added to database")
                break
            elif answer == "n":
                print("user not added to database")
                break
            else:
                print("invalid answer, please answer (y/n)")
                continue

        

def add_user(username, password, pwdb):
    pwdb[username] = password
    return pwdb

username, password = get_credentials()
pwdb = read_pwdb()
authenticate(username, password, pwdb)

