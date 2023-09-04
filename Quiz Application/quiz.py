from database import DatabaseConnector

connection = DatabaseConnector.get_database_connection()
cursor = connection.cursor()

question_query = """
        SELECT * FROM questions;
    """

cursor.execute(question_query)

fields = cursor.fetchall()

questions = [row[1] for row in fields]
options_a = [row[2] for row in fields]
options_b = [row[3] for row in fields]
options_c = [row[4] for row in fields]
options_d = [row[5] for row in fields]
answers = [row[6] for row in fields]

connection.close()

correct_q_count = 0
def prepare_answer(answer):
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
        return 9

print(options_a) 
print("Welcome to quiz, please enter correct option's letter to ",
    "answer questions press q to quit.")

q_index = 0
while q_index < len(fields):

    print(f"\n{q_index+1} - {questions[q_index]}\nA) {options_a[q_index]}\nB)", 
        f"{options_b[q_index]}\nC) {options_c[q_index]}\nD) {options_d[q_index]}\n")
    answer = prepare_answer(input("Answer: "))
    if answer == 0:
        print("Quiz is quitted.")
        break
    elif answer == answers[q_index]:
        correct_q_count += 1
        q_index += 1
    elif answer in (1, 2, 3, 4):
        q_index += 1
    else:
        print("Please enter valid answer.")
    
print(f"\nCorrect answer count: {correct_q_count}")