from user import UserController
import time

class MenuController():
    def __init__(self):
        self.uc = UserController()

    def greet_user(self):
        print("Welcome to quiz application, please enter ",
              "respective number to navigate through the menu.")
        time.sleep(0.75)
        
    def display_first_menu(self):
        print("\n1 - Log in\n2 - Register\n0 - Quit")

    def control_menu(self):
        while True:
            self.display_first_menu()
            navigator = input("Go to: ")

            if navigator == '1':
                self.uc.check_account_inquiry()
            elif navigator == '2':
                self.uc.register_account()
            elif navigator == '0':
                break
            else:
                print("Please enter a valid number.\n")