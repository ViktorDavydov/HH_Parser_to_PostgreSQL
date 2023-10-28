---
--- Creating employer table in cw5_db
---

CREATE TABLE employers WITH VALUES
(
    employer_id int PRIMARY KEY NOT NULL,
    employer_name varchar(20)
);

---
--- Creating vacancies table in cw5_db
---

CREATE TABLE vacancies WITH VALUES
(
    vacancy_id int PRIMARY KEY NOT NULL,

)