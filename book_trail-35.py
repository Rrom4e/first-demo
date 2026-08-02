# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: BookTrail
def get_next_action(user: dict, books: list) -> str:
    """Рекомендует следующее действие на основе текущего состояния."""
    unread = [b for b in books if b.get("status") == "unread"]
    reading = [b for b in books if b.get("status") == "reading"]
    completed = [b for b in books if b.get("status") == "completed"]
    
    if not user and not unread:
        return "Вы завершили все книги. Начните новую!"
    if unread:
        return f"Прочитайте {len(unread)} ещё нераскрытую книгу."
    if reading:
        return f"Закончите чтение текущей книги — {reading[0]['title']}"
    if completed and not user:
        return "Вы прошли все записанные книги. Хотите добавить новую?"
    if user.get("completed_books") > 3:
        return "Поздравляю! Вы уже прочитали более 3 книг."
    return "Продолжайте читать — каждая книга приближает вас к цели!"
