
<p align="center">
  <img src="banner.png" alt="HH Parser Banner" style="max-width: 100%;">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg">
  <img src="https://img.shields.io/badge/Status-In%20progress-yellow">
</p>

# 🛠️ HH Parser — Парсер вакансий с hh.ru | HH.ru Job Vacancy Parser

> 🇷🇺 Русский ниже | 🇬🇧 English above

---

## 🇬🇧 English Description

A simple but powerful Python script that uses the official **hh.ru API** to collect job vacancies based on a keyword and location.

---

### 🔧 Features

- Search vacancies by keyword (e.g., "python junior")
- Support for any region (e.g., Moscow, Saint Petersburg)
- Collects **all pages** of results (not just page 1)
- Saves data to `CSV` or `JSON` by user choice
- Parses job title, salary, city, and link
- Handles Russian text and Unicode correctly

---

### 🚀 How to Run

1. Clone the repository:


git clone https://github.com/Thnktwce/hh-parser.git
cd hh-parser
python hh_parser.py
 
You will be prompted to enter:
🔎 Enter job title: python junior
🏙️ Enter city: Moscow
💾 Save format (csv/json): json
Result will be saved as vacancies.csv or vacancies.json.

💼 Example Output
CSV example:

Title	            Salary	            City	Link
Python Developer	100000 - 150000 RUB	Moscow	https://hh.ru/vacancy/123456

🧰 Technologies
Python 3.10+

requests

hh.ru API

CSV & JSON

🇷🇺 Описание на русском
Простой, но мощный Python-скрипт для сбора вакансий с сайта hh.ru через их официальное API.
Подходит для портфолио, аналитики и автоматизации HR-задач.

🔧 Возможности
Поиск вакансий по ключевому слову (например, "python junior")

Поддержка любого региона (Москва, Питер и др.)

Сбор всех страниц результатов

Сохранение в CSV или JSON на выбор пользователя

Парсинг названия, зарплаты, города и ссылки

Корректная работа с русским текстом

🚀 Как запустить
Клонируйте репозиторий:
git clone https://github.com/Thnktwce/hh-parser.git

cd hh-parser
python hh_parser.py

Программа запросит:
🔎 Введите название вакансии: python junior
🏙️ Введите город (например, Москва): Санкт-Петербург
💾 В каком формате сохранить? (csv/json): csv
Данные сохранятся в vacancies.csv или vacancies.json

💼 Пример результата
Название	        Зарплата	        Город	Ссылка
Python-разработчик	100000 - 150000 RUB	Москва	https://hh.ru/vacancy/123456

🧰 Используемые технологии
Python 3.10+

requests

hh.ru API

CSV и JSON

👨‍💻 Автор / Author
Разработчик: Kirill Kotelyuk @Thnktwce
This project is part of a self-learning portfolio to get a remote job or freelance work in Python.

🏁 License / Лицензия
MIT — free to use and modify.