import sqlite3
import os
import hashlib

curr_user = [""]


def password_check(password):
    if len(password) < 8:
        return False

    if not any(c.isdigit() for c in password) or not any(c.isalpha() for c in password):
        return False

    return True


def add_profile():
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    if website != "" and username != "" and password != "":
        if password_check(password):
            salt = os.urandom(32)
            key = hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),
                salt,
                100000)

            curr_user = current_user(username)
            conn = sqlite3.connect("profiles.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO profiles (user, website, username, password, salt) VALUES (?, ?, ?, ?, ?)",
                           (curr_user, website, username, key, salt))
            conn.commit()
            conn.close()
            print("Data saved.")
        else:
            print("Your password must have least 8 symbols, at least 1 number, at least 1 letter")
    else:
        print("Error! Please, fill all spaces!")


def query_profile():
    username = ""
    website = input("Enter the website: ")
    if website != "":
        conn = sqlite3.connect("profiles.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM profiles WHERE website = ?", (website,))
        result = cursor.fetchone()

        if result:
            cursor.execute("SELECT user FROM profiles WHERE website = ?", (website,))
            user = cursor.fetchone()[0]
            curr_user = current_user(username)
            if user == curr_user:
                print("Website:", result[1])
                print("Username:", result[2])
                print("Password:", result[3])
                conn.close()
            else:
                print("No data found for the specified website.")
                conn.close()
        else:
            print("No data found for the specified website.")
    else:
        print("Error! Please, fill all spaces!")


def delete_profile():
    website = input("Enter the website: ")
    if website != "":
        conn = sqlite3.connect("profiles.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM profiles WHERE website = ?", (website,))
        result = cursor.fetchone()
        if result:
            cursor.execute("DELETE FROM profiles WHERE website = ?", (website,))
            print("Data deleted.")
        else:
            print("No data found for the specified website.")
        conn.commit()
        conn.close()
    else:
        print("Error! Please, fill all spaces!")


def update_profile():
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    if website != "" and username != "" and password != "":
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000)

        conn = sqlite3.connect("profiles.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE profiles SET username = ?, password = ?, salt = ? WHERE website = ?",
                       (username, key, salt, website))
        conn.commit()
        conn.close()
    else:
        print("Error! Please, fill all spaces!")


def add_user():
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    if password_check(password):
        if username != "" and password != "":
            salt = os.urandom(32)
            key = hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),
                salt,
                100000)
            conn = sqlite3.connect("profiles.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, salt) VALUES (?, ?, ?)",
                           (username, key, salt))
            conn.commit()
            conn.close()
            print("Data saved.")
        else:
            print("Error! Please, fill all spaces!")
    else:
        print("Your password must have least 8 symbols, at least 1 number, at least 1 letter")


def authorize():
    conn = sqlite3.connect("profiles.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    result = cursor.fetchone()[0]
    if result != 0:
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        if username != "" and password != "":
            cursor.execute("SELECT username FROM users WHERE username = ?",
                           (username,))
            username_check = cursor.fetchone()[0]
            cursor.execute("SELECT password FROM users WHERE username = ?",
                           (username,))
            key_check = cursor.fetchone()[0]
            cursor.execute("SELECT salt FROM users WHERE username = ?",
                           (username,))
            salt = cursor.fetchone()[0]
            key = hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),
                salt,
                100000)
            if username_check == username and key_check == key:
                print("Authorization successful! Welcome, " + username + "!\n")
                current_user(username)
                conn.commit()
                conn.close()
                return True
            else:
                print("Error! Wrong Data! Please, try again!")
        else:
            print("Error! Please, fill all spaces!")
    else:
        print("No users exists! Please, complete registration!")
    conn.commit()
    conn.close()


def current_user(username):
    if curr_user[0] == "":
        curr_user[0] = username
    else:
        return curr_user[0]


def clear_current_user():
    curr_user[0] = ""
