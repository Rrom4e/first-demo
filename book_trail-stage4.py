# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: BookTrail
def edit_book_record(book_id, new_data):
    """
    Редактирует запись книги по ID.
    new_data: словарь с полями для обновления (например, {'title': 'Новая', 'status': 'reading'}).
    Возвращает обновленную запись или None, если книга не найдена.
    """
    if book_id not in books:
        print(f"Книга с ID {book_id} не найдена.")
        return None

    # Обновляем только те поля, которые переданы в new_data
    for key, value in new_data.items():
        if key in books[book_id]:
            books[book_id][key] = value
        else:
            print(f"Поле '{key}' не существует в этой записи.")

    # Сохраняем изменения (если бы была база данных или файл)
    # Здесь просто возвращаем обновленный объект
    return books[book_id]
