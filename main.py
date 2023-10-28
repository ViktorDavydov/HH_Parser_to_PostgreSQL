import psycopg2
from hh_api_engine import HHApiEngine
from json_manager import HHJsonManager
from config import config
from db_scriptor import DBScriptor
from employees_ids import get_empl_items
from db_manager import DBManager

json_file_name = 'json_vac_info.json'
db_name = 'cw5_db'
ini_config_file = 'database.ini'
section_params = 'postgresql'
script_file = 'create_tables_script.sql'
vacancies_id_dict = get_empl_items()

if __name__ == "__main__":
    print("Привет! Я программа, которая собирает вакансии с лучших компаний HeadHunter!\n"
          "Сейчас в моей базе 10 компаний, а именно: СБЕР, Газпром нефть, 2ГИС, "
          "Центр винного туризма Абрау Дюрсо, VERTEX, КАМАЗ, ФосАгро, Россети Ленэнерго, "
          "Skyeng и Битрикс24\n"
          "Нажмите Enter, чтобы найти и сохранить в базу данных все вакансии "
          "с полной информацией и продолжим!")

    while True:
        user_input = input("> ")
        if user_input != "":
            print("Сперва нажмите Enter!")
        else:
            break
    employee_name = HHApiEngine()
    vacancies_list = employee_name.get_vacancies()  # Получение всех вакансий с ЗП с HeadHunter

    json_instance = HHJsonManager(vacancies_list)
    json_instance.save_to_json(json_file_name)
    print(f"Запись вакансий в библиотеку прошла успешно")
    json_vac_list = json_instance.get_json(json_file_name)

    params = config(ini_config_file, section_params)  # Создание переменной параметров БД

    db_script = DBScriptor()

    db_script.create_db(params, db_name)
    print(f"База данных компаний и вакансий создана")

    params.update({'dbname': db_name})

    connection = psycopg2.connect(**params)
    try:
        with connection as conn:
            with conn.cursor() as cur:
                db_script.create_tables(cur, script_file)
                print(f"Таблицы компаний и вакансий созданы")

                db_script.fill_tables(cur, vacancies_id_dict, json_vac_list)
                print(f"Таблицы компаний и вакансий успешно заполнены")

    finally:
        connection.close()

    connection = psycopg2.connect(**params)
    with connection as conn:
        with conn.cursor() as cur:
            db_manager = DBManager(cur)
            while True:
                print("\nДоступны следующие действия:\n"
                      "1 - Вывести весь список компаний с указанием "
                      "кол-ва найденных вакансий (по убыванию)\n"
                      "2 - Вывести весь список вакансий\n"
                      "3 - Вывести среднюю ЗП по всем вакансиям\n"
                      "4 - Вывести список вакансий у которых ЗП "
                      "выше средней по всем вакансия\n"
                      "5 - Вывести список всех вакансий по ключевому "
                      "слову в названии вакансии\n"
                      "0 - Выйти")
                user_func_input = input("> ")
                if user_func_input == "1":
                    companies = db_manager.get_companies_and_vacancies_count()
                    for company in companies:
                        print(f"Компания: {company[0]}\nКол-во вакансий: {company[1]}")
                        print()

                if user_func_input == "2":
                    vacancies = db_manager.get_all_vacancies()
                    for vacancy in vacancies:
                        print(f"Компания: {vacancy[0]}\nВакансия: {vacancy[1]}\n"
                              f"Зарплата от: {vacancy[2]}\nЗарплата до: {vacancy[3]}\n"
                              f"Ссылка: {vacancy[4]}")
                        print()

                if user_func_input == "3":
                    while True:
                        sal_func_input = input("1 - По зарплате 'от'\n2 - По зарплате 'до'\n> ")
                        if sal_func_input in ("1", "2"):
                            print(f"{round(db_manager.get_avg_salary(sal_func_input)[0][0])} руб.")
                            break
                        else:
                            print("Такой функции нет. Выберите из списка\n")

                if user_func_input == "4":
                    while True:
                        sal_func_input = input("1 - По нижней границе ЗП\n"
                                               "2 - По верхней границе ЗП\n> ")
                        if sal_func_input in ("1", "2"):
                            print(db_manager.get_vacancies_with_higher_salary(sal_func_input))
                            break
                        else:
                            print("Такой функции нет. Выберите из списка\n")


                if user_func_input == "0":
                    print("Пока пока!")
                    break
