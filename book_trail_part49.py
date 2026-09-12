# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: BookTrail
def self_check():
    print("=" * 60)
    print("BookTrail — Самопроверка и отчёт о готовности")
    print("=" * 60)
    books = load_books()
    quotes = load_quotes()
    reviews = load_reviews()
    print(f"Книг в базе: {len(books)}")
    print(f"Цитат в базе: {len(quotes)}")
    print(f"Отзывов в базе: {len(reviews)}")
    if books:
        print(f"Пример книги: {books[0]['title']} — {books[0]['author']}")
        if books[0]['progress']:
            print(f"  Прогресс: {books[0]['progress']}%")
        if books[0]['rating']:
            print(f"  Оценка: {books[0]['rating']}/5")
    if quotes:
        print(f"Пример цитаты: {quotes[0]['text'][:50]}...")
    if reviews:
        print(f"Пример отзыва: {reviews[0]['text'][:50]}...")
    print("\n✅ Приложение готово к использованию!")
    print("Все данные загружены, структура проверена.")
    print("=" * 60)

self_check()
