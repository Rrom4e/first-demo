# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: BookTrail
def _read_book_stats():
    """Return a dict of reading statistics for all books."""
    stats = {}
    for book in books:
        stats[book.title] = {
            'total_pages': book.total_pages,
            'read_pages': sum(book.pages_read),
            'percentage': round(
                (sum(book.pages_read) / book.total_pages) * 100, 2
            ) if book.total_pages else 0,
            'rating': book.rating,
        }
    return stats
