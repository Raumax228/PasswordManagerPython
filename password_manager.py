import sqlite3
import os
import functions
import log
import lang_dict

log.log_start()
if not os.path.exists("profiles.db"):
    conn = sqlite3.connect("profiles.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users ("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "username TEXT, "
                   "password TEXT, "
                   "salt TEXT)")
    cursor.execute("CREATE TABLE profiles ("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "user_id INTEGER, "
                   "website TEXT, "
                   "username TEXT, "
                   "password TEXT, "
                   "salt TEXT, "
                   "FOREIGN KEY (user_id) REFERENCES users(id))")

    conn.commit()
    conn.close()

while True:
    print("\nPassword Manager")
    language = lang_dict.curr_lang.set_language()
    (enter_website, enter_username, enter_password, registration, login, exit, enter_choice, add_rec,
     show_rec, delete_rec, update_rec, invalid_choice, data_saved, password_error, website, username,
     password, no_data, fill_spaces, data_deleted,
     authorization, wrong_data, no_users) = lang_dict.curr_lang.get_dict(language)
    print(f"1. {registration}")
    print(f"2. {login}")
    print(f"3. {exit}")

    choice = input(f"{enter_choice} ")

    if choice == "1":
        functions.add_user()
    elif choice == "2":
        if functions.authorize():
            log.log_in()
            while True:
                print(f"\n1. {add_rec}")
                print(f"2. {show_rec}")
                print(f"3. {delete_rec}")
                print(f"4. {update_rec}")
                print(f"5. {exit}")

                choice = input(f"{exit} ")

                if choice == "1":
                    functions.add_profile()
                elif choice == "2":
                    functions.query_profile()
                elif choice == "3":
                    functions.delete_profile()
                elif choice == "4":
                    functions.update_profile()
                elif choice == "5":
                    log.log_out()
                    break
                else:
                    print(f"{invalid_choice}")
    elif choice == "3":
        log.log_end()
        break
    else:
        print(f"{invalid_choice}")
