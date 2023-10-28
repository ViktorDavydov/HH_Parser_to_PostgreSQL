from abc import ABC, abstractmethod


class ApiEngine(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class JsonManager(ABC):

    @abstractmethod
    def save_to_json(self, json_file_name):
        pass

    @abstractmethod
    def get_json(self, json_file_name):
        pass


class DBCreator(ABC):

    @abstractmethod
    def create_db(self, db_name):
        pass

    @abstractmethod
    def execute_sql_script(self, cursor, fill_script_file):
        pass
