from database import DatabaseConnector

class QuizController():
    def __init__(self):   
        self.quiz_id = 0
        self.quiz_category = ""
        self.question_ids = []     
        self.questions = []
        self.opt_a = []
        self.opt_b = [] 
        self.opt_c = []
        self.opt_d = []
        self.answers = []
        self.quiz_ids = []
        self.quiz_categories = []
        self.quiz_question_ids = []
    
    def prepare_question_parameters(self, questions):
        self.question_ids = [row[0] for row in questions]
        self.questions = [row[1] for row in questions]
        self.opt_a = [row[2] for row in questions]
        self.opt_b = [row[3] for row in questions]
        self.opt_c = [row[4] for row in questions]
        self.opt_d = [row[5] for row in questions]
        self.answers = [row[6] for row in questions]

    def prepare_quiz_parameters(self, quizes):
        self.quiz_ids = [row[0] for row in quizes]
        self.quiz_categories = [row[1] for row in quizes]

    def prepare_quiz_questions(self, quiz_id):
        for id in self.quiz_ids:
            if quiz_id == str(id):
                quiz_query = f""" SELECT * FROM quizes
                    WHERE quiz_id = {id} """ 
                record = DatabaseConnector.get_records(quiz_query)
                i = 0
                self.quiz_question_ids = []
                while i < 20: # works only if quiz has 20 questions
                    self.quiz_question_ids += [field[i+2] for field in record]
                    i += 1

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

    def control_quiz(self, q_given_answers):
        all_questions_index = 0
        quiz_question_index = 0
        correct_q_count = 0
    
        while quiz_question_index < len(self.quiz_question_ids): # WATCH OUT STACK OVERFLOW!
            if (self.quiz_question_ids[quiz_question_index] 
                != self.question_ids[all_questions_index]): 
                all_questions_index += 1
                continue # only works correctly if ids are ordered ascendingly

            print(self.get_question(all_questions_index, quiz_question_index))
            answer = self.convert_answer_to_number(input("Answer: "))

            if answer == self.answers[all_questions_index]:
                quiz_question_index += 1
                correct_q_count += 1
                all_questions_index += 1
                q_given_answers.append(answer)
            elif answer in (1, 2, 3, 4):
                quiz_question_index += 1
                all_questions_index += 1
                q_given_answers.append(answer)
            elif answer == 0:
                print("Quiz is quitted.")
                break
            else:
                print("Please enter a valid answer.")
        
        self.show_results(quiz_question_index, correct_q_count)

    def get_question(self, q_index, q_number):
        return (f"\n{q_number+1} - {self.questions[q_index]}\n"
                f"A) {self.opt_a[q_index]}\nB) {self.opt_b[q_index]}\n"
                f"C) {self.opt_c[q_index]}\nD) {self.opt_d[q_index]}\n")
    
    def show_results(self, q_index, correct_q_count):
        s = 's' if q_index != 1 else ''
        print(f"\n{q_index} question{s} answered"
              f"\nCorrect answer count: {correct_q_count}")
        
    def get_question_indexes(self, quiz_category):
        quiz_query = f""" SELECT * FROM quizes
                    WHERE quiz_category = '{quiz_category}' """ 
        the_quiz = DatabaseConnector.get_records(quiz_query)
        the_quiz = list(the_quiz[0])

        i = 2
        question_indexes = []
        while i < 22:
            question_indexes.append(the_quiz[i])
            
            i += 1
        return question_indexes
    
    def get_quiz_query(self, question_indexes):
        questions_query = "SELECT * FROM questions WHERE question_id IN ("
        i = 0
        for index in question_indexes:
            questions_query += str(index)
            i += 1
            if i < len(question_indexes):
                questions_query += ", "
            
        questions_query += ");"
        print(questions_query)
        return questions_query
    
    def show_quiz_answers(self, questions_query, quiz_result):
        questions = self.get_quiz_questions(questions_query)
        i = 4
        for q in questions:
            if q[6] == quiz_result[i]:
                print(f"Question: {q[1]} | Answer correct: {quiz_result[i]}")
            else:
                print(f"Question: {q[1]} | Incorrect answer: {quiz_result[i]},"
                      f" correct answer was {q[6]}")
            i += 1

    def get_quiz_questions(self, questions_query):
        questions = DatabaseConnector.get_records(questions_query)
        return questions    