from hh_api_engine import HHApiEngine
from json_manager import HHJsonManager
from config import config
from db_creator import create_database

import json

employee_name = HHApiEngine()
# print(json.dumps(employee_name.get_vacancies(), indent=2, ensure_ascii=False))
vacancies_list = employee_name.get_vacancies()

json_instance = HHJsonManager(vacancies_list)
json_instance.save_to_json()


script_file = 'fill_db.sql'
json_file = 'json_vac_info.json'
db_name = 'cw5_db'
ini_config_file = 'database.ini'
section_params = 'postgresql'

params = config(ini_config_file, section_params)
conn = None

create_database(params, db_name)
print(f"БД {db_name} успешно создана")


