# === Stage 39: Добавь документационную строку с описанием сценариев использования ===
# Project: BookTrail
def get_usage_scenarios():
    """
    BookTrail supports several reading scenarios:
    - Daily habit: read a few pages and log progress.
    - Book review: finish a book, add a rating and a quote.
    - Reading list: track planned books and mark them as read.
    - Comparison: compare ratings across books.
    """
    return [
        "Daily habit tracking",
        "Post-reading review with rating and quote",
        "Planned reading list with progress",
        "Cross-book rating comparison",
    ]
