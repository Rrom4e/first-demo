# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: BookTrail
def migrate_structure(current_version, target_version):
    """
    Миграция структуры данных: добавляет метку версии и базовый прогресс.
    current_version — текущая версия структуры (интеграл от предыдущих этапов).
    target_version — целевая версия (текущий этап 46).
    """
    if current_version < target_version:
        if 'version' not in structure:
            structure['version'] = current_version
        if 'books' not in structure or not isinstance(structure.get('books'), list):
            structure['books'] = []
        if 'quotes' not in structure or not isinstance(structure.get('quotes'), list):
            structure['quotes'] = []
        if 'reviews' not in structure or not isinstance(structure.get('reviews'), list):
            structure['reviews'] = []
        if 'reading_progress' not in structure:
            structure['reading_progress'] = {}
        structure['version'] = target_version
        print(f"Миграция выполнена: {current_version} -> {target_version}")
    return structure
