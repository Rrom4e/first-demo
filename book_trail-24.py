# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: BookTrail
def print_book_record(book):
    if not book:
        print("Книга не найдена.")
        return
    print(f"Название: {book['title']}")
    print(f"Автор: {', '.join(book.get('author', []))}")
    print(f"Статус чтения: {'Читаю' if book.get('reading') else 'Прочитана'}")
    print(f"Прогресс: {int(book['progress']['read_pages'])} / {book['progress']['total_pages']} страниц ({book['progress']['percent']:.1f}%)")
    print(f"Оценка: {'⭐' * int(book.get('rating', 0))}")
    if book.get('quotes'):
        print("Цитаты:")
        for q in book['quotes']:
            print(f"  - {q['text']} [{q.get('page', 'не указано')}]")
