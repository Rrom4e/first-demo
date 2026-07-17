# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: BookTrail
def _validate_date(date_str):
    """Проверяет дату в формате 'YYYY-MM-DD' и возвращает datetime или ошибку."""
    from datetime import datetime
    if not date_str or len(date_str) != 10:
        raise ValueError("Некорректный формат даты. Используйте YYYY-MM-DD")
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(f"Ошибка даты '{date_str}': неверная дата (месяц > 12 или день > 31)")
