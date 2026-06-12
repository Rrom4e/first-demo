# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: BookTrail
def filter_books(status=None, category=None, tags=None):
    filtered = books.copy()
    if status:
        filtered = [b for b in filtered if b.get('status') == status]
    if category:
        filtered = [b for b in filtered if b.get('category') == category]
    if tags:
        def has_any_tag(book, tag):
            return any(tag.lower() in t.lower() for t in book.get('tags', []))
        filtered = [b for b in filtered if not tags or has_any_tag(b, tags)]
    return filtered
