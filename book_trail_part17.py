# === Stage 17: Добавь группировку записей по категориям ===
# Project: BookTrail
def group_by_category(records):
    categories = {}
    for record in records:
        cat = record.get('category', 'Uncategorized')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(record)
    return categories
