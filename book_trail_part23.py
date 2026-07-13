# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: BookTrail
def print_reading_report(books):
    """Compact table-style console report for the BookTrail reading tracker."""
    if not books:
        print("No books tracked yet.")
        return
    total_pages = sum(b['pages'] or 0 for b in books)
    completed = len([b for b in books if (b.get('status') or '').lower() == 'finished'])
    avg_progress = (completed / total_pages * 100) if total_pages else 0
    print(f"{'Book':<25} {'Progress':>6} | {'Rating':>4}")
    for b in books:
        title = b.get('title', '')[:23] + ('...' if len(b.get('title','')) > 25 else '')
        pages = b.get('pages') or '?'
        rating = str(b.get('rating', ''))[:3].rjust(4)
        print(f"{title:<25} {pages:>6} | {rating}")
    print("-" * 50)
    print(f"{'Total pages read':<25} {'Avg progress':>12} | {'Books done':>8}")
    print(f"{total_pages:<25} {avg_progress:5.0f}% | {completed:>8}")
