# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: BookTrail
import json, os, sys

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки в структуру проекта."""
    try:
        data = json.loads(json_string)
        
        # Валидация обязательных полей
        required_fields = ['books', 'user_profile']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Отсутствует обязательное поле: {field}")
            
            # Проверка структуры книг
            if not isinstance(data['books'], list):
                raise TypeError("Поле 'books' должно быть списком")
                
            for book in data['books']:
                if not all(k in book for k in ['title', 'author', 'status']):
                    raise ValueError(f"Книга '{book.get('title')}' имеет некорректную структуру")

        # Валидация профиля пользователя
        profile = data['user_profile']
        if not isinstance(profile, dict):
            raise TypeError("Поле 'user_profile' должно быть словарем")
            
        if 'name' not in profile or not isinstance(profile.get('reading_speed'), (int, float)):
            raise ValueError("Некорректный профиль пользователя")

        # Сохранение в глобальное хранилище проекта (если используется) или возврат объекта
        sys.modules[__name__].initial_data = data
        
        return data
    
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        raise
