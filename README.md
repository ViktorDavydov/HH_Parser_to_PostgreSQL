# Парсер вакансий HeadHunter с интеграцией СУБД PostgreSQL

### Установка:
- Убедитесь, что у вас установлен python 3.11 или более новая версия<br>
- Склонировать репозиторий<br>
- Создать и активировать виртуальное окружение```python -m venv ваша_папка_для_виртуального_окружения```<br>
- Установить зависимости командой ```pip install -r requirements.txt```<br>

### Используемые библиотеки:
- requests<br>
- psycopg2<br>

### Логика работы системы:
Данная программа предназначена для сбора вакансий и работы с полученными вакансиями.

Поиск вакансий осуществляется только с указанной зарплатой по следующим компаниям СБЕР, 
Газпром нефть, 2ГИС, Центр винного туризма Абрау Дюрсо, VERTEX, КАМАЗ, ФосАгро, Россети Ленэнерго, 
Skyeng и Битрикс24.

После запуска программы необходимо нажать Enter для поиска вакансий, создания базы данных
и запись вакансий в таблицы базы данных:

Далее выводится контекстное меню в котором необходимо выбрать функцию:
- 1 - Вывести весь список компаний с указанием кол-ва найденных вакансий (по убыванию)
- 2 - Вывести весь список вакансий
- 3 - Вывести среднюю ЗП по всем вакансиям (1 - По зарплате 'от', 2 - По зарплате 'до')
- 4 - Вывести список вакансий у которых ЗП выше средней по всем вакансия (1 - По нижней границе ЗП, 2 - По верхней границе ЗП)
- 5 - Вывести список всех вакансий по ключевому слову в названии вакансии
- 0 - Выйти