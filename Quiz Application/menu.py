from user import UserController
from quiz import QuizController
import time

class MenuController():
    def __init__(self, user_class, quiz_class):
        self.user_class = user_class
        self.quiz_class = quiz_class

    def greet_user(self):
        print("Welcome to quiz application, please enter ",
              "respective number to navigate through the menu.")
        time.sleep(0.75)
        
    def display_first_menu(self):
        print("\n1 - Log in\n2 - Register\n0 - Quit")

    def display_second_menu(self):
        print("\n1 - Solve quiz!\n2 - Review quiz score\n0 - Log out")
     
    def control_menu(self):
        while True:

            if not self.user_class.is_logged_in:
                self.display_first_menu()
                navigator = input("Go to: ")

                if navigator == '1':
                    self.user_class.check_account_inquiry()
                elif navigator == '2':
                    self.user_class.register_account()
                elif navigator == '0':
                    break
                else:
                    print("Please enter a valid number.\n")
            else:
                self.display_second_menu()
                navigator = input("Go to: ")
                
                if navigator == '1':
                    print("Welcome to quiz, please enter correct option's letter to ",
                        "answer questions press q to quit.")
                    self.qc.control_quiz()
                elif navigator == '2':
                    pass
                elif navigator == '0':
                    print("\nLogged out.")
                    self.user_class.is_logged_in = False
                else:
                    print("Please enter a valid number.\n")