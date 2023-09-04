from database import DatabaseConnector

class QuizController():
    def __init__(self):        
        self.questions = []
        self.opt_a = []
        self.opt_b = [] 
        self.opt_c = []
        self.opt_d = []
        self.answers = []
        self.question_count = 0

        self.question_query = """
        SELECT * FROM questions;
    """
        
    def get_question_records(self, query):
        connection = DatabaseConnector.get_database_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        connection.close()
        return records
    
    def prepare_question_parameters(self, records):
        self.question_count = len(records)
        self.questions = [row[1] for row in records]
        self.opt_a = [row[2] for row in records]
        self.opt_b = [row[3] for row in records]
        self.opt_c = [row[4] for row in records]
        self.opt_d = [row[5] for row in records]
        self.answers = [row[6] for row in records]

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

    def control_quiz(self):
        q_index = 0
        correct_q_count = 0
        while q_index < self.question_count:
            print(self.get_question(q_index))
            answer = self.convert_answer_to_number(input("Answer: "))

            if answer == self.answers[q_index]:
                correct_q_count += 1
                q_index += 1
            elif answer in (1, 2, 3, 4):
                q_index += 1
            elif answer == 0:
                print("Quiz is quitted.")
                break
            else:
                print("Please enter valid answer.")

        self.show_results(q_index, correct_q_count)

    def get_question(self, q_index):
        return (f"\n{q_index+1} - {self.questions[q_index]}\n"
                f"A) {self.opt_a[q_index]}\nB) {self.opt_b[q_index]}\n"
                f"C) {self.opt_c[q_index]}\nD) {self.opt_d[q_index]}\n")
    
    def show_results(self, q_index, correct_q_count):
        s = 's' if q_index != 1 else ''
        print(f"\n{q_index} question{s} answered"
              f"\nCorrect answer count: {correct_q_count}")