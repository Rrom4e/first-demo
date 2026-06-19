# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: BookTrail
def export_state():
    import json
    state = {
        "books": [
            {
                "title": b["title"],
                "author": b["author"],
                "progress_percent": round((b.get("pages_read", 0) / b.get("total_pages", 1)) * 100, 2),
                "rating": b.get("rating"),
                "notes": b.get("notes", ""),
            } for b in books_list
        ],
        "stats": {
            "total_books": len(books_list),
            "completed_count": sum(1 for b in books_list if b.get("status") == "finished"),
            "average_rating": round(sum(b.get("rating", 0) for b in books_list if b.get("rating")) / max(len([b for b in books_list if b.get("rating")]), 1), 2),
        }
    }
    return json.dumps(state, indent=2, ensure_ascii=False)
