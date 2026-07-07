# === Stage 20: Добавь восстановление записей из архива ===
# Project: BookTrail
def archive_to_records(archive_path, records):
    """Restore reading records from a JSON archive file."""
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            archive = json.load(f)
        
        if isinstance(archive, list):
            for record in archive:
                records.append(record)
        elif isinstance(archive, dict) and 'records' in archive:
            for record in archive['records']:
                records.append(record)
    except FileNotFoundError:
        pass
