import psycopg2
from config import ConfigClass

class DatabaseConnector():

    @staticmethod
    def get_database_connection():
        return psycopg2.connect(
        dbname="quiz_db",
        user=ConfigClass.get_username(),
        password="3204965",
        host="localhost",
        port="5432"
        )

    @staticmethod
    def get_records(query):
        connection = DatabaseConnector.get_database_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        connection.close()
        return records
    
    @staticmethod
    def insert_record(query, record_values):
        connection = DatabaseConnector.get_database_connection()
        cursor = connection.cursor()
        cursor.execute(query, record_values)
        connection.commit()
        connection.close()