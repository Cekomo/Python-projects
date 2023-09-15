from database import DatabaseConnector

class QuizResultController():
    def __init__(self):
        self.solved_quiz_type = ""
        self.quiz_result_record = []
        self.solved_quiz_types = []
        self.quiz_ids = []
        self.quiz_categories = []
        self.solved_quizes = []

    def save_result(self, user_id, category, quiz_id, users_answers):
        result_query = f""" INSERT INTO quiz_results(user_id, quiz_id, quiz_category, q_answer_1, 
        q_answer_2, q_answer_3, q_answer_4, q_answer_5, q_answer_6, q_answer_7, q_answer_8,
        q_answer_9, q_answer_10, q_answer_11, q_answer_12, q_answer_13, q_answer_14, 
        q_answer_15, q_answer_16, q_answer_17, q_answer_18, q_answer_19, q_answer_20)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
            %s, %s, %s, %s, %s, %s); """
        result_values = (user_id, quiz_id, category) + tuple(users_answers) + \
                (None,) * (20 - len(users_answers))

        DatabaseConnector.insert_record(result_query, result_values)

    def prepare_result_list(self, user_id):
        solved_quizes_query = f"""
            SELECT * FROM quiz_results
            WHERE user_id = {user_id}
            ORDER BY quiz_category ASC;
        """
        self.solved_quizes = DatabaseConnector.get_records(solved_quizes_query)
        self.quiz_ids = [row[2] for row in self.solved_quizes]
        self.quiz_categories = [row[3] for row in self.solved_quizes]

    def show_solved_quizes(self):
        i = 1
        for category in self.quiz_categories:
            print(f"{i} - {category}")
            i += 1

    def prepare_quiz_parameters(self, result_index):
        self.quiz_result_record = self.solved_quizes[result_index]
        self.solved_quiz_type = self.quiz_result_record[3]
    
    def show_quiz_answers(self, questions, quiz_result):
        i = 4
        for q in questions:
            if q[6] == quiz_result[i]:
                print(f"Question: {q[1]} | Answer correct: {quiz_result[i]}")
            else:
                print(f"Question: {q[1]} | Incorrect answer: {quiz_result[i]},"
                      f" correct answer was {q[6]}")
            i += 1