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
        print("\n1 - Select quiz!\n2 - Review quiz score\n0 - Log out")
     
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
                    print("What type of quiz would you like to solve? "
                          "Please enter respective number.\n")
                    i = 1
                    for category in self.quiz_class.quiz_categories:
                        print(f"{i} - {category}")
                        i += 1

                    navigator = input("Solve: ")
                    self.quiz_class.prepare_quiz_questions(navigator)
                    self.quiz_class.control_quiz()
                    
                elif navigator == '2':
                    pass
                elif navigator == '0':
                    print("\nLogged out.")
                    self.user_class.is_logged_in = False
                else:
                    print("Please enter a valid number.\n")