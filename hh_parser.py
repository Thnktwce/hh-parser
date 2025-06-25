import requests
import json
import csv


def get_area_id_by_name(city_name):
    url = "https://api.hh.ru/areas"
    response = requests.get(url)
    regions = response.json()

    for country in regions:
        for region in country["areas"]:
            if city_name.lower() in region["name"].lower():
                return region["id"]
            for city in region["areas"]:
                if city_name.lower() in city["name"].lower():
                    return city["id"]
    return 1  # по умолчанию Москва


def get_all_vacancies(keyword, area_id):
    url = "https://api.hh.ru/vacancies"
    page = 0
    per_page = 20
    all_vacancies = []

    while True:
        params = {"text": keyword, "area": area_id, "per_page": per_page, "page": page}

        response = requests.get(url, params=params)
        data = response.json()

        vacancies = data.get("items", [])
        if not vacancies:
            break

        all_vacancies.extend(vacancies)

        if page >= data.get("pages", 0) - 1:
            break

        page += 1

    return all_vacancies


def save_to_csv(vacancies, filename="vacancies.csv"):
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Название", "Зарплата", "Город", "Ссылка"])

        for vacancy in vacancies:
            name = vacancy["name"]
            salary = vacancy.get("salary")
            if salary:
                _from = salary.get("from") or ""
                _to = salary.get("to") or ""
                currency = salary.get("currency") or ""
                salary_str = f"{_from} - {_to} {currency}".strip()
            else:
                salary_str = "Не указано"

            city = vacancy["area"]["name"]
            link = vacancy["alternate_url"]

            writer.writerow([name, salary_str, city, link])

def save_to_json(vacancies, filename="vacancies.json"):
            with open(filename, mode="w", encoding="utf-8") as file:
                json.dump(vacancies, file, indent=4, ensure_ascii=False)            


def main():
    keyword = input("🔎 Введите название вакансии: ")
    city = input("🏙️ Введите город (например, Москва): ")
    area_id = get_area_id_by_name(city)
    print(f"📍 Поиск по региону: {city} (area_id = {area_id})")

    vacancies = get_all_vacancies(keyword, area_id)

    if not vacancies:
        print("⚠️ Вакансии не найдены.")
        return

    format_choice = input("💾 В каком формате сохранить? (csv/json): ").strip().lower()

    if format_choice == "json":
        save_to_json(vacancies)
        print(f"✅ Сохранено {len(vacancies)} вакансий в 'vacancies.json'")
    else:
        save_to_csv(vacancies)
        print(f"✅ Сохранено {len(vacancies)} вакансий в 'vacancies.csv'")

