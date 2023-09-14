import time
from utility import UtilityClass as util

class MenuController():
    def __init__(self, user_class, quiz_class, answers_class):
        self.user_class = user_class
        self.quiz_class = quiz_class
        self.answers_class = answers_class

    def greet_user(self):
        print("Welcome to quiz application, please enter ",
              "respective number to navigate through the menu.")
        time.sleep(0.75)
        
    def control_main_menu(self):
        self.greet_user()

        while True:
            if self.user_class.is_logged_in:
                self.display_quiz_menu()
                navigator = util.get_valid_input("Go to: ")                
                self.control_quiz_menu(navigator)
            else:
                self.display_main_menu()
                navigator = util.get_valid_input("Go to: ")
                if navigator == '0': break
                self.control_account_menu(navigator)

    def display_main_menu(self):
        print("\n1 - Log in\n2 - Register\n0 - Quit")

    def display_quiz_menu(self):
        print("\n1 - Select quiz!\n2 - Review quiz score\n0 - Log out")

    def control_account_menu(self, navigator):
        if navigator == '1':
            self.user_class.check_account_inquiry()
        elif navigator == '2':
            self.user_class.register_account()
        else:
            print("Please enter a valid number.")

    def control_quiz_menu(self, navigator):
        if navigator == '1':
            self.start_quiz()
        elif navigator == '2':
            self.show_solved_quizes()
        elif navigator == '0':
            self.user_class.is_logged_in = False
            print("Logged out.")
        else:
            print("Please enter a valid number.")

    def start_quiz(self):
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
        self.answers_class.save_result(self.user_class.user_id, category,
                                    self.quiz_class.quiz_id, q_given_answers)
        
    def show_solved_quizes(self):
        self.answers_class.prepare_result_list(self.user_class.user_id)
        self.answers_class.show_solved_quizes()
        result_index = util.get_valid_input("Select an index: ")
        self.answers_class.prepare_quiz_parameters(int(result_index)-1)
        question_indexes = self.quiz_class.get_question_indexes(
            self.answers_class.solved_quiz_type)
        questions_query = self.quiz_class.get_quiz_query(question_indexes)
        self.quiz_class.show_quiz_answers(
            questions_query, 
            self.answers_class.quiz_result_record) 