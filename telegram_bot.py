from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("7605375703:AAGjhUbGYp475ppL1bI86QgodIhiRp3SwFM")
import logging
import requests
import csv
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    ConversationHandler,
    filters,
)


logging.basicConfig(level=logging.INFO)
VACANCY, CITY = range(2)


# Получение area_id по названию города
def get_area_id_by_name(city_name):
    url = "https://api.hh.ru/areas"
    response = requests.get(url)
    for country in response.json():
        for region in country["areas"]:
            if city_name.lower() in region["name"].lower():
                return region["id"]
            for city in region["areas"]:
                if city_name.lower() in city["name"].lower():
                    return city["id"]
    return 1  # Москва


# Получение вакансий
def get_all_vacancies(keyword, area_id):
    url = "https://api.hh.ru/vacancies"
    page = 0
    all_vacancies = []
    while True:
        params = {"text": keyword, "area": area_id, "per_page": 20, "page": page}
        response = requests.get(url, params=params).json()
        items = response.get("items", [])
        if not items:
            break
        all_vacancies.extend(items)
        if page >= response.get("pages", 0) - 1:
            break
        page += 1
    return all_vacancies


# Сохранение в CSV
def save_to_csv(vacancies, filename="vacancies.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Название", "Зарплата", "Город", "Ссылка"])
        for v in vacancies:
            name = v["name"]
            area = v["area"]["name"]
            link = v["alternate_url"]
            salary = v.get("salary")
            if salary:
                _from = salary.get("from") or ""
                _to = salary.get("to") or ""
                currency = salary.get("currency") or ""
                salary_str = f"{_from} - {_to} {currency}".strip()
            else:
                salary_str = "Не указано"
            writer.writerow([name, salary_str, area, link])


# Шаг 1: старт
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 Введите ключевое слово (например, Python):")
    return VACANCY


# Шаг 2: ввод вакансии
async def get_vacancy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["vacancy"] = update.message.text.strip()
    await update.message.reply_text("🏙️ Введите город:")
    return CITY


# Шаг 3: ввод города и выдача вакансий
async def get_city(update: Update, context: ContextTypes.DEFAULT_TYPE):
    vacancy = context.user_data["vacancy"]
    city = update.message.text.strip()
    area_id = get_area_id_by_name(city)
    vacancies = get_all_vacancies(vacancy, area_id)

    if not vacancies:
        await update.message.reply_text("❌ Вакансий не найдено.")
        return ConversationHandler.END

    # Отправим 3 вакансии
    for v in vacancies[:3]:
        name = v["name"]
        link = v["alternate_url"]
        area = v["area"]["name"]
        salary = v.get("salary")
        if salary:
            _from = salary.get("from") or ""
            _to = salary.get("to") or ""
            currency = salary.get("currency") or ""
            salary_str = f"{_from} - {_to} {currency}".strip()
        else:
            salary_str = "Не указано"

        msg = f"💼 {name}\n📍 {area}\n💰 {salary_str}\n🔗 {link}"
        await update.message.reply_text(msg)

    # Сохраняем и отправляем CSV
    save_to_csv(vacancies)
    await update.message.reply_document(
        document=open("vacancies.csv", "rb"),
        filename="vacancies.csv",
        caption="📁 Все вакансии в CSV",
    )

    return ConversationHandler.END


# Обработка /cancel
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❌ Поиск отменён.", reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


# Запуск бота
def main():
    app = ApplicationBuilder().token(API_TOKEN).build()

    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            VACANCY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_vacancy)],
            CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_city)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv)
    app.run_polling()


if __name__ == "__main__":
    main()
