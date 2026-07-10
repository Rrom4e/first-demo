# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: BookTrail
def check_overdue_reminders():
    """Проверяет просроченные напоминания о чтении и выводит список."""
    if not books:
        print("Список книг пуст.")
        return
    today = datetime.date.today()
    overdue = []
    for i, book in enumerate(books):
        target_date = book.get('target_date')
        read_status = book.get('read_status', 'pending')
        if (target_date and isinstance(target_date, str) and
                len(target_date) == 10 and
                read_status != 'done' and
                datetime.date.fromisoformat(target_date) < today):
            overdue.append((i + 1, book['title'], target_date))
    if overdue:
        print(f"\n⚠️  Просроченные напоминания ({len(overdue)} книг):")
        for num, title, date in overdue:
            diff = (today - datetime.date.fromisoformat(date)).days
            print(f"  {num}. '{title}' — была запланирована на {date} "
                  f"(пропущено {diff} дней)")
    else:
        print("✅ Все напоминания в срок!")
