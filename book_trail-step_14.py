# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: BookTrail
def generate_summary():
    if not books: return "Нет данных для сводки."
    total_pages = sum(b.pages for b in books)
    read_progress = (sum(b.readed for b in books) / total_pages * 100) if total_pages else 0
    avg_rating = sum(b.rating for b in books if b.rating) / len([b for b in books if b.rating]) if any(b.rating for b in books) else "N/A"
    top_books = sorted(books, key=lambda x: (x.readed/x.pages*100 if x.pages else 0), reverse=True)[:3]
    quotes_count = sum(len(q.text) > 0 for q in all_quotes)
    return f"Прочитано книг: {len([b for b in books if b.readed])}/{len(books)} ({read_progress:.1f}%)\nСтраницы: {sum(b.pages for b in books if b.readed)}/{total_pages}\nСредняя оценка: {avg_rating}\nТоп-3 книги по прогрессу: {[b.title for b in top_books]}\nЦитат сохранено: {quotes_count}"
