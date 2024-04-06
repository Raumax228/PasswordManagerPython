class Language:
    def __init__(self):
        self.language = ""

    @staticmethod
    def set_language():
        language = input("Please choose a language (eng/rus): ").lower()
        if language == "eng":
            return eng
        elif language == "rus":
            return rus
        else:
            print("Invalid language choice. Using English as default.")
            return eng

    @staticmethod
    def get_dict(language):
        enter_website = language["enter_website"]
        enter_username = language["enter_username"]
        enter_password = language["enter_password"]
        registration = language["registration"]
        login = language["login"]
        exit = language["exit"]
        enter_choice = language["enter_choice"]
        add_rec = language["add_record"]
        show_rec = language["show_record"]
        delete_rec = language["delete_record"]
        update_rec = language["update_record"]
        invalid_choice = language["invalid_choice"]
        data_saved = language["data_saved"]
        password_error = language["password_error"]
        website = language["website"]
        username = language["username"]
        password = language["password"]
        no_data = language["no_data"]
        fill_spaces = language["fill_spaces"]
        data_deleted = language["data_deleted"]
        authorization = language["authorization"]
        wrong_data = language["wrong_data"]
        no_users = language["no_users"]

        return (enter_website, enter_username, enter_password, registration, login, exit, enter_choice, add_rec,
                show_rec, delete_rec, update_rec, invalid_choice, data_saved, password_error, website, username,
                password, no_data, fill_spaces, data_deleted, authorization, wrong_data, no_users)


curr_lang = Language()

eng = {
    "enter_website": "Enter the website:",
    "enter_username": "Enter the username:",
    "enter_password": "Enter the password:",
    "registration": "Registration",
    "login": "Log in",
    "exit": "Exit",
    "enter_choice": "Enter your choice: ",
    "add_record": "Add record",
    "show_record": "Show record",
    "delete_record": "Delete record",
    "update_record": "Update record",
    "invalid_choice": "Invalid choice. Please try again.",
    "data_saved": "Data saved.",
    "password_error": "Your password must have least 8 symbols, at least 1 number, at least 1 letter",
    "website": "Website:",
    "username": "Username:",
    "password": "Password:",
    "no_data": "No data found for the specified website.",
    "fill_spaces": "Error! Please, fill all spaces!",
    "data_deleted": "Data deleted.",
    "authorization": "Authorization successful! Welcome, ",
    "wrong_data": "Error! Wrong Data! Please, try again!",
    "no_users": "No users exists! Please, complete registration!"

}

rus = {
    "enter_website": "Введите адрес сайта:",
    "enter_username": "Введите имя пользователя:",
    "enter_password": "Введите пароль:",
    "registration": "Регистрация",
    "login": "Войти в аккаунт",
    "exit": "Выход",
    "enter_choice": "Введите ваш выбор: ",
    "add_record": "Добавить данные",
    "show_record": "Показать данные",
    "delete_record": "Удалить данные",
    "update_record": "Обновить данные",
    "invalid_choice": "Неправильный выбор. Пожалуйста, попробуйте еще раз.",
    "data_saved": "Данные сохранены.",
    "password_error": "Ваш пароль должен состоять как минимум из 8 символов, иметь хотя бы 1 цифру и хотя бы 1 букву",
    "website": "Вебсайт:",
    "username": "Имя пользователя:",
    "password": "Пароль:",
    "no_data": "Не найдены данные для введеного вебсайта.",
    "fill_spaces": "Ошибка! Пожалуйста, заполните все поля!",
    "data_deleted": "Данные удалены.",
    "authorization": "Авторизация успешна! Добро пожаловать, ",
    "wrong_data": "Ошибка! Неверные данные! Пожалуйста, попробуйте снова!",
    "no_users": "Пользователей не существует! Пожалуйста, пройдите регистрацию!"
}
