# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: BookTrail
class Book:
    def __init__(self, title, author, pages=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.read_progress = 0
        self.ratings = []
        self.quotes = []

    def add_rating(self, rating):
        if not isinstance(rating, (int, float)) or not 1 <= rating <= 5:
            raise ValueError("Оценка должна быть числом от 1 до 5.")
        self.ratings.append(rating)

    def add_quote(self, text):
        if len(text.strip()) < 3:
            raise ValueError("Цитата должна содержать минимум 3 символа.")
        self.quotes.append(text)

    def set_progress(self, pages_read):
        if not isinstance(pages_read, int) or pages_read < 0:
            raise ValueError("Количество прочитанных страниц должно быть неотрицательным целым числом.")
        total = self.pages
        if total > 0:
            self.read_progress = min(pages_read, total)
        else:
            self.read_progress = pages_read

    def get_average_rating(self):
        if not self.ratings:
            return None
        return sum(self.ratings) / len(self.ratings)


def validate_book_input(title, author, pages):
    if not title or not isinstance(title, str):
        raise ValueError("Название книги должно быть непустой строкой.")
    if not author or not isinstance(author, str):
        raise ValueError("Автор должен быть непустой строкой.")
    if not isinstance(pages, int) or pages < 0:
        raise ValueError("Количество страниц должно быть неотрицательным целым числом.")
    return Book(title.strip(), author.strip(), pages)
