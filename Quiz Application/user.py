from database import DatabaseConnector
import time

class UserController():
    def __init__(self):
        self.username = ""
        self.password = ""
        self.usernames = []
        self.password = []

    def prepare_account_parameters(self, records):
        self.usernames = [row[1] for row in records]
        self.passwords = [row[2] for row in records]

    def control_account_inquiry(self):
        while True:
            print("\nPlease enter username and password to login.")
            time.sleep(0.75)
            self.username = input("Username: ")
            self.password = input("Password: ")

            if self.is_logged_in():
                print("\nLogin succesful.")
                break
            else:
                print("Wrong username or password.")

    
    def is_logged_in(self):
        acc_index = 0
        for u in self.usernames:
            if self.username == u and self.password == self.passwords[acc_index]:
                return True
            
            acc_index += 1

        return False

