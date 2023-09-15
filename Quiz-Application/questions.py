from database import DatabaseConnector as DC

class QuestionController():
    def __init__(self):
        self.question_ids = []     
        self.question_texts = []
        self.options_a = []
        self.options_b = [] 
        self.options_c = []
        self.options_d = []
        self.answers = []

    def prepare_question_parameters(self, questions): 
        # it seems it fetches whole data for each question call
        self.question_ids = [row[0] for row in questions]
        self.questions = [row[1] for row in questions]
        self.options_a = [row[2] for row in questions]
        self.options_b = [row[3] for row in questions]
        self.options_c = [row[4] for row in questions]
        self.options_d = [row[5] for row in questions]
        self.answers = [row[6] for row in questions]

    @staticmethod
    def get_question(instance, q_index, q_number):
        return (f"\n{q_number+1} - {instance.questions[q_index]}\n"
                f"A) {instance.options_a[q_index]}\nB) {instance.options_b[q_index]}\n"
                f"C) {instance.options_c[q_index]}\nD) {instance.options_d[q_index]}\n")
    
    @staticmethod
    def get_question_indexes(quiz_category):
        quiz_query = f""" SELECT * FROM quizes
                    WHERE quiz_category = '{quiz_category}' """ 
        the_quiz = DC.get_records(quiz_query)
        the_quiz = list(the_quiz[0])

        i = 2
        question_indexes = []
        while i < 22:
            question_indexes.append(the_quiz[i])
            i += 1
        return question_indexes