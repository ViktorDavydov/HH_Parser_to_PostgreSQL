class DBManager:

    def __init__(self, cursor):
        self.cursor = cursor

    def get_companies_and_vacancies_count(self):
        self.cursor.execute("SELECT employer_name, COUNT(*) AS vacancies_count "
                            "FROM vacancies "
                            "INNER JOIN employers USING(employer_id) "
                            "GROUP BY employer_name "
                            "ORDER BY vacancies_count DESC")

        return self.cursor.fetchall()

    def get_all_vacancies(self):
        self.cursor.execute("SELECT employer_name, vacancy_name, vacancy_salary_from, "
                            "vacancy_salary_to, vacancy_url "
                            "FROM vacancies "
                            "INNER JOIN employers USING(employer_id)")

        return self.cursor.fetchall()

    def get_avg_salary(self, func_num):
        if func_num == "1":
            self.cursor.execute("SELECT AVG(vacancy_salary_from) FROM vacancies")
        elif func_num == "2":
            self.cursor.execute("SELECT AVG(vacancy_salary_to) FROM vacancies")

        return self.cursor.fetchall()

    def get_vacancies_with_higher_salary(self, func_sal_num):
        if func_sal_num == "1":
            self.cursor.execute("SELECT vacancy_id, vacancy_name, employer_id, "
                                "vacancy_salary_from, vacancy_url FROM vacancies "
                                "INNER JOIN employers USING(employer_id) "
                                "WHERE vacancy_name IS NOT NULL "
                                "GROUP BY vacancy_id, vacancy_name, employer_id, "
                                "vacancy_salary_from, vacancy_url "
                                "HAVING vacancy_salary_from > (SELECT AVG(vacancy_salary_from) "
                                "FROM vacancies)")

        elif func_sal_num == "2":
            self.cursor.execute("SELECT vacancy_id, vacancy_name, employer_id, "
                                "vacancy_salary_to, vacancy_url FROM vacancies "
                                "INNER JOIN employers USING(employer_id) "
                                "WHERE vacancy_name IS NOT NULL "
                                "GROUP BY vacancy_id, vacancy_name, employer_id, "
                                "vacancy_salary_to, vacancy_url "
                                "HAVING vacancy_salary_to > (SELECT AVG(vacancy_salary_to) "
                                "FROM vacancies)")

        return self.cursor.fetchall()

