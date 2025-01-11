from datetime import datetime

def get_days_from_today(date):
    """
    Розраховує кількість днів між заданою датою і поточною датою.

    :param date: str, дата у форматі 'РРРР-ММ-ДД'
    :return: int або None, кількість днів між заданою датою і поточною датою,
             або None, якщо формат дати некоректний
    """
    try:
        # рядок  у дату
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        # Отримання поточної дати
        today_date = datetime.today().date()
        # Обчислення різниці у днях
        delta = input_date - today_date
        return delta.days
    except Exception:
        # Якщо сталася помилка, повернути None
        return None

# Приклади використання функції
if __name__ == "__main__":
    # минулому
    print(get_days_from_today("2020-10-09"))  # Наприклад: -1189 (залежить від поточної дати)
    #  майбутньому
    print(get_days_from_today("2025-10-09"))  # Наприклад: 272 (залежить від поточної дати)
    # Невірний формат
    print(get_days_from_today("10/09/2021"))  # None
    # Інший невірний формат
    print(get_days_from_today("incorrect-format"))  # None
