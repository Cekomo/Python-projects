import psycopg2

class DatabaseConnector():

    @staticmethod
    def get_database_connection():
        return psycopg2.connect(
        dbname="quiz_db",
        user="postgres",
        password="3204965",
        host="localhost",
        port="5432"
        )


    