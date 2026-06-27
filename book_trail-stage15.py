# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: BookTrail
def get_weekly_stats(data):
    from datetime import date, timedelta
    if not data: return {}
    stats = {}
    for entry in data:
        d = date.fromisoformat(entry['date'])
        week_start = (d - timedelta(days=d.weekday())).isoformat()
        key = f"{entry['book_id']}:{week_start}"
        stats[key] = stats.get(key, {'reads': 0, 'pages': 0})
        stats[key]['reads'] += entry.get('read_count', 1)
        stats[key]['pages'] += entry.get('pages_read', 0)
    return stats
