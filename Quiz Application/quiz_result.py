from database import DatabaseConnector

class QuizAnswersController():
    def __init__(self):
        pass

    def save_result(self, user_id, quiz_id, users_answers):
        result_query = f""" INSERT INTO user_quiz_results(user_id, quiz_id, q_answer_1, 
        q_answer_2, q_answer_3, q_answer_4, q_answer_5, q_answer_6, q_answer_7, q_answer_8,
        q_answer_9, q_answer_10, q_answer_11, q_answer_12, q_answer_13, q_answer_14, 
        q_answer_15, q_answer_16, q_answer_17, q_answer_18, q_answer_19, q_answer_20)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
            %s, %s, %s, %s, %s); """
        result_values = (user_id, quiz_id) + tuple(users_answers) + \
                (None,) * (20 - len(users_answers))

        DatabaseConnector.insert_record(result_query, result_values)

    