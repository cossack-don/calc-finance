import datetime

# Получаем текущую дату
today = datetime.datetime.now()
current_month = today.month
current_year = today.year

def is_leap_year(current_year):
    """Определяет, является ли год високосным"""
    return (current_year % 400 == 0) or (current_year % 100 != 0 and current_year % 4 == 0)

month_days = {
    "january": 31,
    "february": 29 if is_leap_year(current_year) else 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}

def get_count_days_from_current_month(current_month):
    return month_days[current_month]