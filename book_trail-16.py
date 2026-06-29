# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: BookTrail
def get_monthly_stats(stats: dict, current_year: int) -> list[tuple[str, float]]:
    monthly = {str(m): 0.0 for m in range(1, 13)}
    total_read = 0.0
    for book_id, data in stats.items():
        if not data.get('completed'):
            continue
        date_str = data.get('finished_at', '')
        if not date_str:
            continue
        try:
            year, month, day = map(int, date_str.split('-')[:3])
            if year == current_year and 1 <= month <= 12:
                monthly[str(month)] += data.get('rating', 0.0)
                total_read += 1
        except ValueError:
            continue
    result = []
    for m in range(1, 13):
        avg_rating = monthly[str(m)] / total_read if total_read > 0 else 0.0
        result.append((f"{current_year}-{m:02d}", round(avg_rating, 2)))
    return sorted(result)
