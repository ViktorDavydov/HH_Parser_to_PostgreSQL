import requests
from abstract_classes import ApiEngine
from employees_ids import get_employees_id_list


class HHApiEngine(ApiEngine):
    """Класс для получения вакансий по API"""

    def __init__(self):
        self.hh_api_url = "https://api.hh.ru"
        self.headers = {
            "User-Agent": "ViktorDavydov"
        }

    def get_vacancies(self):
        """Получение всех вакансий компании"""
        vacancies_list = []
        hh_vac_url = self.hh_api_url + "/vacancies"
        employee_list = get_employees_id_list()
        for num in range(len(employee_list)):
            params = {
                "employer_id": employee_list[num],
                "per_page": 100,
                "only_with_salary": True
            }
            response = requests.get(hh_vac_url, params=params, headers=self.headers)
            if response.status_code == 200:
                vacancies = response.json()
                if len(vacancies_list) == 0:
                    vacancies_list.append(vacancies["items"])
                else:
                    vacancies_list.extend(vacancies["items"])

            #
            #     vacancies = response.json()

        return vacancies_list
