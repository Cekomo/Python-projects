from menu import MenuController
from user import UserController
from questions import QuestionController
from quiz import QuizController
from quiz_result import QuizResultController
from database import DatabaseConnector

uc = UserController()
qsc = QuestionController()
qzc = QuizController(qsc)
ac = QuizResultController()
mc = MenuController(uc, qzc, ac)

account_query = """ SELECT * FROM users; """
records = DatabaseConnector.get_records(account_query)
uc.prepare_account_parameters(records)

question_query = """ SELECT * FROM questions ORDER BY question_id; """
questions_table = DatabaseConnector.get_records(question_query)
qsc.prepare_question_parameters(questions_table)
quiz_query = """ SELECT * FROM quizes; """
questions_table = DatabaseConnector.get_records(quiz_query)
qzc.prepare_quiz_parameters(questions_table)

mc.control_main_menu()