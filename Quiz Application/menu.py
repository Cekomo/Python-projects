import time

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
     
    def control_menu(self):
        while True:

            if not self.user_class.is_logged_in:
                self.display_first_menu()
                navigator = input("Go to: ")
                print()

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
                print()
                
                if navigator == '1':
                    q_given_answers = []
                    print("What type of quiz would you like to solve? "
                          "Please enter respective number.\n")
                    i = 1
                    for category in self.quiz_class.quiz_categories:
                        print(f"{i} - {category}")
                        i += 1

                    while True:
                        category_index = input("Solve: ")
                        if category_index.isdigit(): break
                    category = self.quiz_class.quiz_categories[int(category_index)-1]
                    self.quiz_class.quiz_id = category_index
                    self.quiz_class.prepare_quiz_questions(category_index)
                    self.quiz_class.control_quiz(q_given_answers)
                    self.q_a_class.save_result(self.user_class.user_id, category,
                                               self.quiz_class.quiz_id, q_given_answers)
                    
                elif navigator == '2':
                    self.q_a_class.prepare_result_list(self.user_class.user_id)
                    self.q_a_class.show_solved_quizes()
                    while True:
                        result_index = input("Select an index: ")
                        if result_index.isdigit(): break
                        
                    self.q_a_class.show_quiz_result(int(result_index)-1)
                    print(self.quiz_class.get_quiz_answer_key(self.q_a_class.solved_quiz_type))
                    
                elif navigator == '0':
                    print("Logged out.")
                    self.user_class.is_logged_in = False
                else:
                    print("Please enter a valid number.\n")