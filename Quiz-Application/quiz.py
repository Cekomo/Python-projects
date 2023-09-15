from database import DatabaseConnector

class QuizController():
    def __init__(self, question_class):   
        self.QSC = question_class

        self.quiz_id = 0
        self.quiz_category = ""
        self.quiz_ids = []
        self.quiz_categories = []
        self.quiz_question_ids = []

    def prepare_quiz_parameters(self, quizes):
        self.quiz_ids = [row[0] for row in quizes]
        self.quiz_categories = [row[1] for row in quizes]

    def prepare_quiz_questions(self, quiz_id):
        the_id = ""
        for id in self.quiz_ids:
            if quiz_id == str(id):
                the_id = id

        quiz_query = f""" SELECT * FROM quizes
            WHERE quiz_id = {the_id}; """ 
        record = DatabaseConnector.get_records(quiz_query)
        i = 0
        question_ids = []
        while i < 20: # works only if quiz has 20 questions
            question_ids += [field[i+2] for field in record]
            i += 1
        self.quiz_question_ids = sorted(question_ids)
        print(self.quiz_question_ids)
            
    def convert_answer_to_number(self, answer):
        if answer in ('a','A','1'):
            return 1
        elif answer in ('b','B','2'):
            return 2
        elif answer in ('c','C','3'):
            return 3
        elif answer in ('d','D','4'):
            return 4
        elif answer in ('q', 'Q'):
            return 0
        else:   
            return -1

    def operate_quiz(self, q_given_answers):
        all_questions_index = 0
        quiz_question_index = 0
        correct_q_count = 0
    
        while quiz_question_index < len(self.quiz_question_ids):
            if (self.quiz_question_ids[quiz_question_index] # requires ascending order
                != self.QSC.question_ids[all_questions_index]): 
                all_questions_index += 1
                continue 

            print(self.QSC.get_question(self.QSC, all_questions_index, quiz_question_index))
            answer = self.convert_answer_to_number(input("Answer: "))

            if answer == 0:
                print("Quiz is quitted.")
                break
            elif answer not in (1, 2, 3, 4):
                print("Please enter a valid answer.")
                continue

            quiz_question_index += 1
            all_questions_index += 1
            q_given_answers.append(answer)
            if answer == self.QSC.answers[all_questions_index]:
                correct_q_count += 1
        
        self.show_results(quiz_question_index, correct_q_count)

    def show_results(self, q_index, correct_q_count):
        s = 's' if q_index != 1 else ''
        print(f"\n{q_index} question{s} answered"
              f"\nCorrect answer count: {correct_q_count}")
        
    def get_quiz_query(self, question_indexes):
        questions_query = "SELECT * FROM questions WHERE question_id IN ("
        i = 0
        for index in question_indexes:
            questions_query += str(index)
            i += 1
            if i < len(question_indexes):
                questions_query += ", "
            
        questions_query += ");"
        return questions_query
    
    def get_quiz_questions_record(self, questions_query):
        questions = DatabaseConnector.get_records(questions_query)
        return questions    