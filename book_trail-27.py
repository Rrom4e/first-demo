# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: BookTrail
def reset_demo_data():
    """Возвращает BookTrail к дефолтным данным."""
    global books, quotes, ratings, current_book_idx
    books = [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "pages": 180},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "pages": 296},
        {"title": "1984", "author": "George Orwell", "pages": 328},
    ]
    quotes = [
        "So we beat on, boats against the current...",
        "The one thing that you mustn't... is be afraid.",
        "War is peace. Freedom is slavery. Ignorance is strength."
    ]
    ratings = {}
    current_book_idx = 0

def clear_state():
    """Очищает все данные и возвращает в исходное состояние."""
    reset_demo_data()
