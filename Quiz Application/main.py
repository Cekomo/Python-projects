from menu import MenuController
from user import UserController
from quiz import QuizController
from database import DatabaseConnector

mc = MenuController()
uc = UserController()
qc = QuizController()

mc.greet_user()
mc.control_menu()

account_query = """ SELECT * FROM users; """
records = DatabaseConnector.get_records(account_query)
uc.prepare_account_parameters(records)
uc.check_account_inquiry()

print("Welcome to quiz, please enter correct option's letter to ",
    "answer questions press q to quit.")

question_query = """ SELECT * FROM questions; """
records = DatabaseConnector.get_records(question_query)
qc.prepare_question_parameters(records)
qc.control_quiz()