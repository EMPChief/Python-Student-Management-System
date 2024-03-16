import mysql.connector
import dotenv
import os

dotenv.load_dotenv()

class DatabaseConnection:
    def __init__(self):
        self.username = os.getenv("MYSQL_USER")
        self.password = os.getenv("MYSQL_PASSWORD")
        self.host = os.getenv("MYSQL_HOST")
        self.database = os.getenv("MYSQL_DATABASE")

    def connect(self):
        connection = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.database,
            auth_plugin='mysql_native_password'
        )
        return connection
