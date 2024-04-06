import sqlite3
import os
import hashlib
import lang_dict


class CurrUser:
    def __init__(self):
        self.user = ""

    def set_current_user(self, user_id):
        self.user = user_id

    def get_current_user(self):
        return self.user


class Passwords:
    def __init__(self):
        self.key = b""
        self.salt = b""

    @staticmethod
    def password_check(password_inp):
        if len(password_inp) < 8:
            return False

        if not any(c.isdigit() for c in password_inp) or not any(c.isalpha() for c in password_inp):
            return False

        return True

    def hash_password(self, password_inp):
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password_inp.encode('utf-8'),
            salt,
            100000)
        self.key = key
        self.salt = salt


curr_user = CurrUser()
passwords = Passwords()

language = lang_dict.curr_lang.set_language()
(enter_website, enter_username, enter_password, registration, login, exit, enter_choice, add_rec,
 show_rec, delete_rec, update_rec, invalid_choice, data_saved, password_error, website, username,
 password, no_data, fill_spaces, data_deleted,
 authorization, wrong_data, no_users) = lang_dict.curr_lang.get_dict(language)


def add_profile():
    user_id = curr_user.get_current_user()
    website_inp = input(f"{enter_website} ")
    username_inp = input(f"{enter_username} ")
    password_inp = input(f"{enter_password} ")
    if website_inp != "" and username_inp != "" and password_inp != "":
        if passwords.password_check(password_inp):
            passwords.hash_password(password_inp)
            key = passwords.key
            salt = passwords.salt
            conn = sqlite3.connect("profiles.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO profiles (user_id, website, username, password, salt) VALUES (?, ?, ?, ?, ?)",
                           (user_id, website_inp, username_inp, key, salt))
            conn.commit()
            conn.close()
            print(f"{data_saved}")
        else:
            print(f"{password_error}")
    else:
        print(f"{fill_spaces}")


def query_profile():
    website_inp = input(f"{enter_website} ")
    if website_inp != "":
        conn = sqlite3.connect("profiles.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM profiles WHERE website = ?", (website_inp,))
        result = cursor.fetchone()

        if result:
            cursor.execute("SELECT user_id FROM profiles WHERE website = ?", (website_inp,))
            user_id = cursor.fetchone()[0]
            curr_user_id = curr_user.get_current_user()
            if user_id == curr_user_id:
                print(f"{website}", result[2])
                print(f"{username}", result[3])
                print(f"{password}", result[4])
                conn.close()
            else:
                print(f"{no_data}")
                conn.close()
        else:
            print(f"{no_data}")
    else:
        print(f"{fill_spaces}")


def delete_profile():
    website_inp = input(f"{enter_website} ")
    if website_inp != "":
        conn = sqlite3.connect("profiles.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM profiles WHERE website = ?", (website_inp,))
        result = cursor.fetchone()
        if result:
            cursor.execute("DELETE FROM profiles WHERE website = ?", (website_inp,))
            print(f"{data_deleted}")
        else:
            print(f"{no_data}")
        conn.commit()
        conn.close()
    else:
        print(f"{fill_spaces}")


def update_profile():
    website_inp = input(f"{enter_website} ")
    username_inp = input(f"{enter_username} ")
    password_inp = input(f"{enter_password} ")
    if website_inp != "" and username_inp != "" and password_inp != "":
        if passwords.password_check(password_inp):
            passwords.hash_password(password_inp)
            key = passwords.key
            salt = passwords.salt
            conn = sqlite3.connect("profiles.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE profiles SET username = ?, password = ?, salt = ? WHERE website = ?",
                           (username_inp, key, salt, website_inp))
            conn.commit()
            conn.close()
        else:
            print(f"{password_error}")
    else:
        print(f"{fill_spaces}")


def add_user():
    username_inp = input(f"{enter_username} ")
    password_inp = input(f"{enter_password} ")
    if username_inp != "" and password_inp != "":
        if passwords.password_check(password_inp):
            passwords.hash_password(password_inp)
            key = passwords.key
            salt = passwords.salt
            conn = sqlite3.connect("profiles.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, salt) VALUES (?, ?, ?)",
                           (username_inp, key, salt))
            conn.commit()
            conn.close()
            print(f"{data_saved}")
        else:
            print(f"{password_error}")
    else:
        print(f"{fill_spaces}")


def authorize():
    conn = sqlite3.connect("profiles.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    result = cursor.fetchone()[0]
    if result != 0:
        username_inp = input(f"{enter_username} ")
        password_inp = input(f"{enter_password} ")
        if username_inp != "" and password_inp != "":
            cursor.execute("SELECT username FROM users WHERE username = ?",
                           (username_inp,))
            username_check = cursor.fetchone()[0]
            cursor.execute("SELECT password FROM users WHERE username = ?",
                           (username_inp,))
            key_check = cursor.fetchone()[0]
            cursor.execute("SELECT salt FROM users WHERE username = ?",
                           (username_inp,))
            salt = cursor.fetchone()[0]
            key = hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),
                salt,
                100000)
            if username_check == username_inp and key_check == key:
                print(f"{authorization} {username}!\n")
                cursor.execute("SELECT id FROM users WHERE username = ?",
                               (username_inp,))
                user_id = cursor.fetchone()
                curr_user.set_current_user(user_id[0])
                conn.commit()
                conn.close()
                return True
            else:
                print(f"{wrong_data}")
        else:
            print(f"{fill_spaces}")
    else:
        print(f"{no_users}")
    conn.commit()
    conn.close()
