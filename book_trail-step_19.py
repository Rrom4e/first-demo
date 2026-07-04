# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: BookTrail
def archive_old_records(min_days=365, status='completed'):
    from datetime import datetime, timedelta
    cutoff_date = datetime.now() - timedelta(days=min_days)
    archived_count = 0
    for book in books:
        if book['status'] == status and (book.get('last_read', None) is not None):
            last_read_dt = datetime.strptime(book['last_read'], '%Y-%m-%d')
            if last_read_dt < cutoff_date:
                book['archived'] = True
                archived_count += 1
    print(f"Archived {archived_count} old records.")
