# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: BookTrail
import json, os

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return {}
    except json.JSONDecodeError:
        print("Ошибка: файл содержит некорректный JSON.")
        return {}

if __name__ == "__main__":
    data = load_data('books.json')
    if not data:
        exit(1)
    
    for book in data.values():
        progress = int(book.get('progress', 0))
        total_pages = int(book.get('total_pages', 0))
        
        print(f"\nКнига: {book['title']}")
        if total_pages > 0:
            percent = (progress / total_pages) * 100
            status = "Читаю" if progress < total_pages else "Прочитано"
            print(f"Статус: {status} ({percent:.1f}% завершено)")
        else:
            print("Страниц не указано.")
