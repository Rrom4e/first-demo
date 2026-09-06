# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: BookTrail
def backup_data(filepath):
    """Создаёт резервную копию файла данных с таймстампом."""
    import shutil
    from datetime import datetime
    backup_path = f"{filepath}.bak_{datetime.now():%Y%m%d_%H%M%S}"
    shutil.copy2(filepath, backup_path)
    print(f"Резервная копия сохранена: {backup_path}")
    return backup_path
