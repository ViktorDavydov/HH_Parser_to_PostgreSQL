import psycopg2
from abstract_classes import DBCreator


class DBScriptor(DBCreator):

    def __init__(self, params):
        self.params = params

    def create_db(self, db_name) -> None:
        """Создает новую базу данных."""
        try:
            connection = psycopg2.connect(host=self.params['host'],
                                          user=self.params['user'],
                                          password=self.params['password'],
                                          port=self.params['port'])
            connection.autocommit = True
            cur = connection.cursor()
            cur.execute(f"DROP DATABASE IF EXISTS {db_name};")
            cur.execute(f"CREATE DATABASE {db_name};")

        finally:
            connection.close()

    def execute_sql_script(self, cursor, fill_script_file) -> None:
        """Выполняет скрипт из файла для заполнения БД данными."""
        with open(fill_script_file, 'r') as file:
            cursor.execute(file.read())
