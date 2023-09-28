from database import DatabaseConnector

class QuizResultController():
    def __init__(self):
        self.solved_quiz_type = ""
        self.previous_quiz_correct_answer = 0
        self.solved_quiz_count = 0
        self.quiz_result_record = []
        self.solved_quiz_types = []
        self.quiz_ids = []
        self.quiz_categories = []
        self.solved_quizes = []
        

    def save_result(self, user_id, category, quiz_id, user_answers, correct_answers):
        
        if not self.is_category_solved(user_id, category):
            result_query = f""" INSERT INTO quiz_results(user_id, quiz_id, quiz_category, 
            correct_answer_count, q_answer_1, q_answer_2, q_answer_3, q_answer_4, 
            q_answer_5, q_answer_6, q_answer_7, q_answer_8, q_answer_9, q_answer_10, 
            q_answer_11, q_answer_12, q_answer_13, q_answer_14, q_answer_15, q_answer_16, 
            q_answer_17, q_answer_18, q_answer_19, q_answer_20)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s); """
        elif correct_answers > self.previous_quiz_correct_answer:
            result_query = f""" UPDATE quiz_results SET user_id = %s, quiz_id = %s,
            quiz_category = %s, correct_answer_count = %s, q_answer_1 = %s,
            q_answer_2 = %s,q_answer_3 = %s, q_answer_4 = %s, q_answer_5 = %s, 
            q_answer_6 = %s, q_answer_7 = %s, q_answer_8 = %s, q_answer_9 = %s, 
            q_answer_10 = %s, q_answer_11 = %s, q_answer_12 = %s, q_answer_13 = %s, 
            q_answer_14 = %s, q_answer_15 = %s, q_answer_16 = %s, q_answer_17 = %s, 
            q_answer_18 = %s, q_answer_19 = %s, q_answer_20 = %s
            WHERE user_id = {user_id} AND quiz_category = '{category}'; """
        else:
            return
        
        result_values = (user_id, quiz_id, category, correct_answers) + \
                    tuple(user_answers) + (None,) * (20 - len(user_answers))
        DatabaseConnector.insert_record(result_query, result_values)

    def prepare_solved_quiz_list(self, user_id):
        solved_quizes_query = f"""
            SELECT * FROM quiz_results
            WHERE user_id = {user_id}
            ORDER BY quiz_category ASC;
        """
        self.solved_quizes = DatabaseConnector.get_records(solved_quizes_query)
        self.quiz_ids = [row[2] for row in self.solved_quizes]
        self.quiz_categories = [row[3] for row in self.solved_quizes]

    def show_solved_quiz_list(self):
        i = 0
        self.solved_quiz_types = []
        for category in self.quiz_categories:
            i += 1
            print(f"{i} - {category}")
            self.solved_quiz_types.append(category)

        self.solved_quiz_count = i

    def prepare_solved_quiz_parameters(self, result_index):
        self.quiz_result_record = self.solved_quizes[result_index]
        self.solved_quiz_type = self.quiz_result_record[3]
    
    def show_solved_quiz_evaluation(self, questions, quiz_result):
        correct_answer_count = 0
        i = 5
        for q in questions:
            if quiz_result[i] == None:
                break
            if q[6] == quiz_result[i]:
                print(f"Question: {q[1]} | Answer correct: {quiz_result[i]}")
                correct_answer_count += 1
            else:
                print(f"Question: {q[1]} | Incorrect answer: {quiz_result[i]},"
                      f" correct answer was {q[6]}")
            i += 1

        self.calculate_quiz_result(i - 4, correct_answer_count)

    def get_correct_answer_count(self, questions, quiz_result):
        answer_index = 0
        correct_answer_counter = 0
        for q in questions:
            if answer_index >= len(quiz_result): 
                break
            if q[6] == quiz_result[answer_index]:
                correct_answer_counter += 1
            answer_index += 1

        return correct_answer_counter
            
    def get_solved_quiz_result(self, user_id, quiz_category):
        result_category_query = f"""
            SELECT * FROM quiz_results 
            WHERE user_id = {user_id} AND
            quiz_category = '{quiz_category}' """
        
        solved_quiz_record = DatabaseConnector.get_records(
            result_category_query)
        return solved_quiz_record
    
    def is_category_solved(self, user_id, quiz_category):
        solved_quiz_record = self.get_solved_quiz_result(user_id, quiz_category)
        try:
            self.previous_quiz_correct_answer = int(solved_quiz_record[0][4])
        except:
            self.previous_quiz_correct_answer = 0

        return True if self.previous_quiz_correct_answer != 0 else False

    def set_solved_quiz_type(self, category_index):
        quiz_query = f""" SELECT * FROM quizes
                    WHERE quiz_id = {category_index} """
        solved_quiz_record = DatabaseConnector.get_records(quiz_query)
        self.solved_quiz_type = solved_quiz_record[0][1]

    def calculate_quiz_result(self, questions_solved, correct_answer_count):
        total_question_count = 20
        question_point = 100 / total_question_count

        print(f"\n{questions_solved} question(s) solved."
            f"\nYour score is: {question_point*correct_answer_count}")
        if correct_answer_count >= int(0.7 * total_question_count):
            print("You have successfuly completed the quiz.")
        else:
            print("You failed. At least 70% of the of the questions "
                  "must be answered correctly to pass the test.")