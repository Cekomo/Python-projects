from menu import MenuController
from user import UserController
from quiz import QuizController
from quiz_result import QuizResultController
from database import DatabaseConnector

uc = UserController()
qc = QuizController()
ac = QuizResultController()
mc = MenuController(uc, qc, ac)

account_query = """ SELECT * FROM users; """
records = DatabaseConnector.get_records(account_query)
uc.prepare_account_parameters(records)

question_query = """ SELECT * FROM questions ORDER BY question_id; """
records = DatabaseConnector.get_records(question_query)
qc.prepare_question_parameters(records)
quiz_query = """ SELECT * FROM quizes; """
records = DatabaseConnector.get_records(quiz_query)
qc.prepare_quiz_parameters(records)

mc.greet_user()
mc.control_menu()