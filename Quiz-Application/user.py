from database import DatabaseConnector
from questions import QuestionController

class UserController():
    def __init__(self):
        self.is_logged_in = False
        self.user_id = 0
        self.username = ""
        self.password = ""
        self.user_ids = []
        self.usernames = []
        self.password = []

    def prepare_account_parameters(self, records):
        self.user_ids = [row[0] for row in records]
        self.usernames = [row[1] for row in records]
        self.passwords = [row[2] for row in records]

    def check_account_inquiry(self):
        while True:
            print("Please enter username and password to login.")
            self.username = input("Username: ").lower()
            self.password = input("Password: ")

            if self.is_login_successful():
                self.is_logged_in = True
                print("\nLogin succesful.")
                break
            else:
                print("Wrong username or password.")
        
    def are_infos_valid(self, username, password):
        if not 6 <= len(username) <= 11 and not username.isalpha():
            return False
        
        if len(password) != 6 and not username.isdigit():
            return False
        
        return True

    def is_login_successful(self):
        acc_index = 0
        for u in self.usernames:
            # print(self.username == u, self.password == self.passwords[acc_index])
            if self.username == u and self.password == self.passwords[acc_index]:
                self.user_id = self.user_ids[acc_index]        
                return True
            
            acc_index += 1

        return False

    def register_account(self):
        print("\nPlease enter username and password to sign up.\n"
              "Username can only be consist of letters (6-11 characters) "
              "and only numbers can be used for password (6 characters)")
        username = input("Username: ").lower()
        password = password = input("Password: ")
        password_again = password = input("Password again: ")

        if password != password_again:
            print("Passwords do NOT match.")
        elif self.are_infos_valid(username, password):
            self.save_account(username, password)
            print("Account is created!")
            return

    def save_account(self, username, password):
        register_query = f"""
            INSERT INTO users(username, password, quiz_taken, quiz_successful)
            VALUES (%s, %s, %s, %s); """
        
        register_values = (str(username), password, 0, 0)
        DatabaseConnector.insert_record(register_query, register_values)