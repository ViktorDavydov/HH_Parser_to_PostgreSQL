DROP TABLE IF EXISTS employers;
DROP TABLE IF EXISTS vacancies;

---
--- Creating employer table in cw5_db
---

CREATE TABLE employers (
    employer_id int PRIMARY KEY NOT NULL,
    employer_name varchar(20)
);

---
--- Creating vacancies table in cw5_db
---

CREATE TABLE vacancies (
    vacancy_id int PRIMARY KEY NOT NULL,
    vacancy_name varchar(50),
    vacancy_salary_from int NOT NULL,
    vacancy_salary_to int NOT NULL,
    vacancy_url text
);