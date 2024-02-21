import sqlite3
import os
import functions

if not os.path.exists("profiles.db"):
    conn = sqlite3.connect("profiles.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE profiles ("
                   "user TEXT, "
                   "website TEXT, "
                   "username TEXT, "
                   "password TEXT, "
                   "salt TEXT)")
    cursor.execute("CREATE TABLE users ("
                   "username TEXT, "
                   "password TEXT, "
                   "salt TEXT)")
    conn.commit()
    conn.close()

while True:
    print("\nPassword Manager")
    print("1. Registration")
    print("2. Log in")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        functions.add_user()
    elif choice == "2":
        if functions.authorize():
            while True:
                print("\n1. Add Record")
                print("2. Show Record")
                print("3. Delete Record")
                print("4. Update Record")
                print("5. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    functions.add_profile()
                elif choice == "2":
                    functions.query_profile()
                elif choice == "3":
                    functions.delete_profile()
                elif choice == "4":
                    functions.update_profile()
                elif choice == "5":
                    functions.clear_current_user()
                    break
                else:
                    print("Invalid choice. Please try again.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
