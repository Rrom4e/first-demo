# === Stage 32: Добавь журнал действий пользователя ===
# Project: BookTrail
class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, action_type, book=None, detail=""):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action_type,
            "book": book.title if book else None,
            "detail": detail,
        }
        self.entries.append(entry)

    def get_recent(self, limit=10):
        return list(reversed(self.entries[-limit:]))

    def clear(self):
        self.entries.clear()


# Подключение к журналу действий в BookTrail
actions = ActionLog()
