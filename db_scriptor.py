import psycopg2
import json
from abstract_classes import DBOperator


class DBScriptor(DBOperator):

    def __init__(self):
        pass

    def create_db(self, params, db_name) -> None:
        """Создает новую базу данных."""
        connection = psycopg2.connect(**params)
        connection.autocommit = True
        cur = connection.cursor()
        cur.execute(f"DROP DATABASE IF EXISTS {db_name};")
        cur.execute(f"CREATE DATABASE {db_name};")
        cur.close()
        connection.close()

    def create_tables(self, cursor, fill_script_file) -> None:
        """Выполняет скрипт из файла для создания таблиц в БД."""
        with open(fill_script_file, 'r') as file:
            cursor.execute(file.read())

    def fill_tables(self, cursor, vacancies_list: list) -> None:
        for item in vacancies_list:
            cursor.execute(f"INSERT INTO employers VALUES (%s, %s)",
                           (int(item['employer']['id']), item['employer']['name']))

        for item in vacancies_list:
            cursor.execute(f"INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)",
                           (int(item['id']), item['name'], item['salary']['from'],
                            item['salary']['to'], item['alternate_url']))



