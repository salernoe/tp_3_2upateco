import mysql.connector
class DatabaseConnection:
    _connection = None
    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
            host='127.0.0.1',
            user='my_user',
            port = "3306",
            password='my_pass',
            database='my_database'
            )
        return cls._connection
    qwerqewrqw
    