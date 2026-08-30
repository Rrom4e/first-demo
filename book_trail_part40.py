# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: BookTrail
import argparse

def main():
    parser = argparse.ArgumentParser(description="BookTrail - Трекер чтения книг")
    parser.add_argument("--add", nargs="?", const="true", action="store_true", help="Добавить книгу (название)")
    parser.add_argument("--progress", nargs=2, metavar=("BOOK", "PAGES"), help="Обновить прогресс (книга, страницы)")
    parser.add_argument("--quote", nargs=3, metavar=("BOOK", "QUOTE", "PAGE"), help="Добавить цитату")
    parser.add_argument("--rate", nargs=2, metavar=("BOOK", "SCORE"), help="Оценить книгу")
    parser.add_argument("--list", action="store_true", help="Показать все книги")
    parser.add_argument("--search", nargs="?", const="true", action="store_true", help="Поиск по названию")
    args = parser.parse_args()
    if args.add:
        print("Режим добавления книги. Введите название:")
        name = input()
        add_book(name)
    elif args.progress:
        update_progress(args.progress[0], args.progress[1])
    elif args.quote:
        add_quote(args.quote[0], args.quote[1], args.quote[2])
    elif args.rate:
        rate_book(args.rate[0], args.rate[1])
    elif args.list:
        list_books()
    elif args.search:
        search_books()
    else:
        parser.print_help()
