import psycopg2

connection = psycopg2.connect(
    dbname="quiz_db",
    user="postgres",
    password="3204965",
    host="localhost",
    port="5432"
)

query = """
    SELECT * FROM quizes;
"""

cursor = connection.cursor()
cursor.execute(query)

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
    elif answer == 0:
        return 0
    else:   
        print("Please enter valid answer.")
        return 9

print(options_a) 
print("Welcome to quiz, please enter correct option's letter to ",
    "answer questions press 0 to quit.")

q_index = 0
while q_index < len(fields):

    print(f"{questions[q_index]}\nA) {options_a[q_index]}\nB)", 
        f"{options_b[q_index]}\nC) {options_c[q_index]} \nD) {options_d[q_index]}")
    answer = prepare_answer(input("Answer: "))
    if answer == 0:
        break
    elif answer == answers[q_index]:
        correct_q_count += 1
        q_index += 1
    elif answer in (1, 2, 3, 4):
        q_index += 1
    else:
        print("Please enter valid answer.")
    

print(f"\nCorrect answer count: {correct_q_count}")