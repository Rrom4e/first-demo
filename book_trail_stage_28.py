# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: BookTrail
def print_metrics():
    """Compact metrics dashboard for BookTrail."""
    total = len(books)
    finished = sum(1 for b in books if progress(b) == 100)
    avg_page = (sum(p * pages(b) for b, p in zip(books, progress(books))) / total) if total else 0
    ratings = [rating(b) for b in books if rating(b)]
    avg_rating = sum(ratings) / len(ratings) if ratings else 0
    quotes_total = sum(len(qs) for q in all_quotes.values())
    print(f"Books: {total} | Finished: {finished} ({100*finished/max(total,1):.1f}%)")
    print(f"Avg pages read: {avg_page:.1f}")
    print(f"Avg rating: {avg_rating:.2f}" if avg_rating else "No ratings yet")
    print(f"Quotes collected: {quotes_total}")
