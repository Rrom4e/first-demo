# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: BookTrail
def delete_book(book_id: int) -> bool:
    """Удалить книгу по ID, если она существует."""
    if book_id not in books:
        print(f"Книга с id={book_id} не найдена.")
        return False
    
    del books[book_id]
    
    # Удаляем связанные цитаты и оценки для чистоты данных
    for key, value in list(quotes.items()):
        if isinstance(value, dict) and book_id in value.get('books', []):
            del quotes[key]['books'][value['id']]
            if not value['books']: # Если список книг пуст, удаляем цитату целиком (упрощенно: если это была только эта книга)
                del quotes[key]
    
    for key, value in list(ratings.items()):
        if isinstance(value, dict) and book_id in value.get('books', []):
            del ratings[key]['books'][value['id']]
            # Аналогичная логика очистки оценок
    
    print(f"Книга с id={book_id} успешно удалена.")
    return True

def delete_quote(quote_id: int) -> bool:
    """Удалить цитату по ID."""
    if quote_id not in quotes:
        print(f"Цитата с id={quote_id} не найдена.")
        return False
    
    del quotes[quote_id]
    print("Цитата успешно удалена.")
    return True

def delete_rating(rating_id: int) -> bool:
    """Удалить оценку по ID."""
    if rating_id not in ratings:
        print(f"Оценка с id={rating_id} не найдена.")
        return False
    
    del ratings[rating_id]
    print("Оценка успешно удалена.")
    return True
