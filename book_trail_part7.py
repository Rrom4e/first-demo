# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: BookTrail
def sort_books(key='date', reverse=False):
    if key == 'date':
        return sorted(books, key=lambda b: b.get('added_at', ''), reverse=reverse)
    elif key == 'priority':
        return sorted(books, key=lambda b: int(b.get('priority', 0)), reverse=True)
    elif key == 'title':
        return sorted(books, key=lambda b: b.get('title', '').lower())
    else:
        raise ValueError(f"Неизвестный ключ сортировки: {key}")

def get_sorted_books(key='date'):
    try:
        return sort_books(key)
    except Exception as e:
        print(f"Ошибка сортировки: {e}")
        return books
