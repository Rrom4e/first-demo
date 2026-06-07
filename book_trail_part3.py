# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: BookTrail
class BookTracker:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, pages=0, read_pages=0, rating=None, quote=""):
        book = {
            "title": title,
            "author": author,
            "pages": pages,
            "read_pages": read_pages,
            "rating": rating,
            "quote": quote
        }
        self.books.append(book)
        return book

    def get_progress(self):
        if not self.books:
            return 0
        total_pages = sum(b["pages"] for b in self.books if b["pages"] > 0)
        read_total = sum(b["read_pages"] for b in self.books if b["pages"] > 0)
        return (read_total / total_pages * 100) if total_pages > 0 else 0

    def get_books(self):
        return self.books
