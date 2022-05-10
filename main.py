import os
import bcrypt
from database import *


def clear(): return os.system('clear')


connect()


def login():
    print("--- LOGIN ---")
    print("Username :")
    username = input()
    print("Password :")
    password = input().encode('utf-8')
    if check_user(username, password):
        menu()
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
    else:
        clear()
        print("User already exist, please login :\n")
        login()


def menu():
    clear()
    while True:
        print("--- MENU ---")
        print("1. Solo VS AI")
        print("2. Multiplayer")
        choice = input()
        if choice == "1":
            os.system("python3 solo.py")
        elif choice == "2":
            os.system("python3 client.py")
        else:
            clear()
            print("Wrong input")


clear()
while True:
    print("--- MULTIPLAYER ---")
    print("1. Login")
    print("2. Register")
    choice = input()
    if choice == "1":
        login()
    elif choice == "2":
        register()
    else:
        clear()
        print("wrong input\n")
