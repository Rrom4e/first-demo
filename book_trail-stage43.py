# === Stage 43: Добавь пагинацию длинных списков ===
# Project: BookTrail
def paginate(items, per_page=10):
    """Разбивает список на страницы по per_page элементов."""
    pages = []
    for i in range(0, len(items), per_page):
        pages.append(items[i:i + per_page])
    return pages

def get_page(pages, page_num):
    """Возвращает страницу по номеру (начиная с 0)."""
    return pages[page_num] if 0 <= page_num < len(pages) else None

def get_total_pages(pages):
    """Возвращает общее количество страниц."""
    return len(pages)
