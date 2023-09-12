import time
from utility import UtilityClass as util

class MenuController():
    def __init__(self, user_class, quiz_class, answer_class):
        self.user_class = user_class
        self.quiz_class = quiz_class
        self.q_a_class = answer_class

    def greet_user(self):
        print("Welcome to quiz application, please enter ",
              "respective number to navigate through the menu.")
        time.sleep(0.75)
        
    def display_first_menu(self):
        print("\n1 - Log in\n2 - Register\n0 - Quit")

    def display_second_menu(self):
        print("\n1 - Select quiz!\n2 - Review quiz score\n0 - Log out")

    def navigate_on_account(self, navigator):
        if navigator == '1':
            self.user_class.check_account_inquiry()
        elif navigator == '2':
            self.user_class.register_account()
        elif navigator == '0':
            return
        else:
            print("Please enter a valid number.\n")
     
    def control_main_menu(self):
        while True:
            if not self.user_class.is_logged_in:
                self.display_first_menu()
                navigator = util.get_valid_input("Go to:")
                self.navigate_on_account(navigator)
            else:
                self.display_second_menu()
                navigator = util.get_valid_input("Go to:")                
                
                self.control_quiz_menu(navigator)

    def control_quiz_menu(self, navigator):
        if navigator == '1':
            q_given_answers = []
            print("What type of quiz would you like to solve? "
                    "Please enter respective number.\n")
            i = 1
            for category in self.quiz_class.quiz_categories:
                print(f"{i} - {category}")
                i += 1

            category_index = util.get_valid_input("Solve: ")
            category = self.quiz_class.quiz_categories[int(category_index)-1]
            self.quiz_class.quiz_id = category_index
            self.quiz_class.prepare_quiz_questions(category_index)
            self.quiz_class.control_quiz(q_given_answers)
            self.q_a_class.save_result(self.user_class.user_id, category,
                                        self.quiz_class.quiz_id, q_given_answers)
            
        elif navigator == '2':
            self.q_a_class.prepare_result_list(self.user_class.user_id)
            self.q_a_class.show_solved_quizes()
            result_index = util.get_valid_input("Select an index: ")
            self.q_a_class.prepare_quiz_parameters(int(result_index)-1)
            question_indexes = self.quiz_class.get_question_indexes(self.q_a_class.solved_quiz_type)
            questions_query = self.quiz_class.get_quiz_query(question_indexes)
            self.quiz_class.show_quiz_answers(questions_query, self.q_a_class.quiz_result_record) 

        elif navigator == '0':
            print("Logged out.")
            self.user_class.is_logged_in = False
        else:
            print("Please enter a valid number.\n")