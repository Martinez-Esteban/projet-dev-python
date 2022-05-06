from atexit import register
import bcrypt
from os import system, name
from database import *

def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')

   # for mac and linux
   else:
    _ = system('clear')

connect()

def multiplayer():
    clear()
    print("--- MULTIPLAYER ---")
    print("1. Login")
    print("2. Register")
    choice = input()
    if choice == "1":
        clear()
        login()
    elif choice == "2":
        register()
    else:
        clear()
        print("wrong input")
    
def login():
        print("--- LOGIN ---")
        print("Username :")
        username = input()
        print("Password :")
        password = input().encode('utf-8')
        if check_user(username, password):
            system('python3 client.py')
        else:
            clear()
            print("Wrong username or password \n")
            login()

def register():
    clear()
    print("--- REGISTER ---")
    print("Username :")
    username = input()
    print("Password :")
    password = input().encode('utf-8')
    hash = bcrypt.hashpw(password, bcrypt.gensalt())
    if user_not_exist(username):
        add_user(username, hash)
        clear()
        login()
    
while True:
    print("--- MENU ---")
    print("1. Solo VS AI")
    print("2. Multiplayer")
    choice = input()
    if choice == "1":
        system("python3 solo.py")
    elif choice == "2":
        multiplayer()
    else:
        clear()
        print("Wrong input")