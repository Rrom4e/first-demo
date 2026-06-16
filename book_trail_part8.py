# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: BookTrail
def show_menu():
    print("\n=== BookTrail Меню ===")
    print("1. Добавить книгу")
    print("2. Показать прогресс чтения")
    print("3. Оценить прочитанное")
    print("4. Удалить книгу")
    print("5. Выход")
    try:
        choice = input("Выберите действие (1-5): ").strip()
        if not choice.isdigit():
            raise ValueError
        return int(choice)
    except ValueError:
        print("Неверный ввод.")
        return None

def handle_add_book(book_manager, book_db):
    title = input("Название книги: ")
    author = input("Автор: ")
    progress = 0
    while True:
        try:
            p = int(input(f"Прогресс (0-{len(author)}%): "))
            if 0 <= p <= 100:
                break
        except ValueError:
            pass
    book_manager.add_book(title, author, progress)

def handle_show_progress(book_db):
    for title, data in book_db.items():
        print(f"'{title}' ({data['author']}): {data['progress']}%")

def handle_rate_book(book_db):
    title = input("Название книги для оценки: ")
    if title not in book_db:
        return
    rating = int(input("Оценка (1-5): "))
    print(f"Книга '{title}' оценена на {rating}/5")

def handle_delete_book(book_manager, book_db):
    title = input("Название книги для удаления: ")
    if book_manager.remove_book(title):
        del book_db[title]
        print("Книга удалена.")

while True:
    choice = show_menu()
    if choice is None:
        continue
    elif choice == 1:
        handle_add_book(book_manager, book_db)
    elif choice == 2:
        handle_show_progress(book_db)
    elif choice == 3:
        handle_rate_book(book_db)
    elif choice == 4:
        handle_delete_book(book_manager, book_db)
    elif choice == 5:
        print("До встречи!")
        break
