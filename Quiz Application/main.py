from quiz import QuizController

print("Welcome to quiz, please enter correct option's letter to ",
    "answer questions press q to quit.")

qc = QuizController()

records = qc.get_question_records(qc.question_query)
qc.prepare_question_parameters(records)
qc.control_quiz()