
# HH.ru Vacancy Parser 🧠💼

Vacancy parser from hh.ru in Python.  
Gets a list of vacancies by keyword and saves it to a CSV file.

## 📌 Features

- Search jobs by keyword (e.g. `python junior`)
- Retrieve title, salary, city and reference
- Save data to `vacancies.csv`.

---

## 🚀 How to use

### Installation

Requires Python 3.7+ 
Install dependencies:

pip install requests
Run
bash
Copy
Edit
python hh_parser.py
Type in what to look for, for example:

bash
Copy
Edit
Enter the job title to search for: python junior
✅ Saved 20 jobs in 'vacancies.csv'
📝 Example result
Example row in vacancies.csv:

Title Salary City Reference
Junior Python Developer 80 000 - 120 000 RUB Moscow https://hh.ru/vacancy/123456789

💡 Ideas for improvement
Collect all pages (not only 1st page)

Support other regions (area ID)

Saving in JSON

Telegram bot

Flask web-interface

Salary chart by jobs

👤 Author
Kirill Koteluk
🎯 Beginner Python developer. I'm learning the language and creating useful tools for portfolio and remote work.