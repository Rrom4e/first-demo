# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: BookTrail
def demo_run():
    print("=== BookTrail Demo ===")
    books = [
        {"title": "1984", "author": "Orwell", "status": "reading"},
        {"title": "War and Peace", "author": "Tolstoy", "status": "done"},
        {"title": "Dune", "author": "Herbert", "status": "planning"},
    ]
    for b in books:
        print(f"  {b['title']} by {b['author']}: {b['status']}")
    print("Demo complete. Ready for manual testing.")

demo_run()
