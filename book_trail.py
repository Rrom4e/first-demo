# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: BookTrail
import json
from datetime import datetime

class BookTrail:
    def __init__(self):
        self.books = []
        self.last_id = 0
        self.data_file = "booktrail_data.json"

    def load_data(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.books = data.get('books', [])
                self.last_id = data.get('last_id', 0)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump({'books': self.books, 'last_id': self.last_id}, f, ensure_ascii=False, indent=2)

    def add_book(self, title, author, progress=0, rating=None):
        self.last_id += 1
        book = {
            'id': self.last_id,
            'title': title,
            'author': author,
            'progress': progress,
            'rating': rating,
            'completed': progress >= 100,
            'added_at': datetime.now().isoformat()
        }
        self.books.append(book)
        self.save_data()
        return book

    def get_books(self):
        return sorted(self.books, key=lambda x: x['added_at'], reverse=True)

if __name__ == "__main__":
    app = BookTrail()
    app.add_book("1984", "Джордж Оруэлл", 50)
    app.add_book("Мастер и Маргарита", "Михаил Булгаков", 100, 5)
    for book in app.get_books():
        print(f"{book['title']} ({book['author']}) - {book['progress']}%")
