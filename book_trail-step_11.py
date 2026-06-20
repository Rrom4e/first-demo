# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: BookTrail
import json, os

DATA_FILE = "booktrail_data.json"

def save_books(books):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []
