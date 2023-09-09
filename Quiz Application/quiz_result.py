from database import DatabaseConnector

class QuizAnswersController():
    def __init__(self):
        self.solved_quiz_types = []

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

    def show_solved_quizes(self,user_id):
        solved_quizes_query = f"""
            SELECT quiz_id, quiz_category FROM quiz_results
            WHERE user_id = {user_id};
        """
        solved_quizes = DatabaseConnector.get_records(solved_quizes_query)
        quiz_ids = [row[0] for row in solved_quizes]
        quiz_categories = [row[1] for row in solved_quizes]

        i = 1
        for category in quiz_categories:
            print(f"{i} - {category}")


    def show_quiz_result(self, user_id, quiz_id):
        result_query = f"""
            SELECT * FROM quiz_results
            WHERE user_id = {user_id} AND quiz_id = {quiz_id};
        """

