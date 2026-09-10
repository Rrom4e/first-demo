# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: BookTrail
def demo():
    """Показывает основной пользовательский сценарий BookTrail."""
    # Создаём новую книгу
    book = Book(title="1984", author="Оруэлл", year=1949)
    print(f"Создана книга: {book.title} ({book.author}, {book.year})")

    # Добавляем несколько глав
    book.add_chapter("Часть 1", 50)
    book.add_chapter("Часть 2", 40)
    book.add_chapter("Часть 3", 30)
    print(f"Добавлено {len(book.chapters)} глав")

    # Прогресс чтения
    book.read_pages(10)
    book.read_pages(15)
    print(f"Прочитано: {book.pages_read} страниц из {book.total_pages}")
    print(f"Прогресс: {book.progress:.1f}%")

    # Добавляем цитаты
    quote = book.add_quote("Вся власть принадлежит партии.")
    quote.page = 5
    quote.highlight = True
    print(f"Добавлена цитата: {quote.text[:40]}... (выделена: {quote.highlight})")

    # Оценка
    book.rate(5, "Классика антиутопии")
    print(f"Оценка: {book.rating:.1f}/5 — {book.review}")

    # Личные заметки
    note = book.add_note("Будущее может быть хуже настоящего.")
    print(f"Заметка сохранена: {note.text}")

    # Статистика
    print(f"\nСтатистика чтения:")
    print(f"  Всего страниц: {book.total_pages}")
    print(f"  Прочитано: {book.pages_read}")
    print(f"  Оставлено: {book.pages_left}")
    print(f"  Процент: {book.progress:.1f}%")
    print(f"  Цитат: {len(book.quotes)}")
    print(f"  Заметок: {len(book.notes)}")

    # Сохранение
    book.save()
    print(f"\nДанные сохранены в {book.file_path}")

    # Загрузка и проверка
    loaded = Book.load(book.file_path)
    print(f"Загружено: {loaded.title} — {loaded.pages_read} стр. прочитано")
    assert loaded.title == book.title
    assert loaded.pages_read == book.pages_read
    assert loaded.quotes[0].text == quote.text
    assert loaded.rating == book.rating
    print("✓ Все данные сохранены и загружены корректно!")

if __name__ == "__main__":
    demo()
