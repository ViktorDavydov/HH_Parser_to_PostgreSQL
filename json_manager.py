from abstract_classes import JsonManager
import json


class HHJsonManager(JsonManager):

    def __init__(self, vacancies_list):
        self.vacancies_list = vacancies_list

    def save_to_json(self):
        """Сохранение вакансий в json"""
        with open("json_vac_info.json", "w", encoding="utf-8") as file:
            json.dump(self.vacancies_list, file, indent=2, ensure_ascii=False)

    def get_json(self):
        """Получение вакансий из json"""
        with open("json_vac_info.json", "r", encoding="utf-8") as file:
            vacancies_info = json.load(file)
            return vacancies_info
