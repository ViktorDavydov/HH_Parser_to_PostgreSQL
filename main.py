import psycopg2

from hh_api_engine import HHApiEngine
from json_manager import HHJsonManager
from config import config
from db_scriptor import DBScriptor

import json

json_file_name = 'json_vac_info.json'
db_name = 'cw5_db'
ini_config_file = 'database.ini'
section_params = 'postgresql'
script_file = 'create_tables_script.sql'

employee_name = HHApiEngine()
# print(json.dumps(employee_name.get_vacancies(), indent=2, ensure_ascii=False))
vacancies_list = employee_name.get_vacancies()

json_instance = HHJsonManager(vacancies_list)
json_instance.save_to_json(json_file_name)
print(f"Запись вакансий в {json_file_name} прошла успешно")
json_vac_list = json_instance.get_json(json_file_name)

params = config(ini_config_file, section_params)
conn = None

db_script = DBScriptor()

db_script.create_db(params, db_name)
print(f"БД {db_name} создана")

params.update({'dbname': db_name})
connection = psycopg2.connect(**params)
try:
    with connection as conn:
        with conn.cursor() as cur:
            db_script.create_tables(cur, script_file)
            print(f"Таблицы employers и vacancies созданы")

            db_script.fill_tables(cur, json_vac_list)

finally:
    connection.close()
