# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: BookTrail
class Reminder:
    def __init__(self, title, date_due, note=""):
        self.title = title
        self.date_due = date_due  # YYYY-MM-DD
        self.note = note
        self.done = False
    
    def is_overdue(self):
        from datetime import date as dt_date
        return dt_date.today() > dt_date.fromisoformat(self.date_due) if not self.done else False
    
    def __repr__(self):
        status = "✅" if self.done else "⏳"
        overdue = " 🔴" if self.is_overdue() and not self.done else ""
        return f"{status} {self.title} — до: {self.date_due}{overdue}"

class ReminderManager:
    def __init__(self):
        self.reminders = []
    
    def add(self, title, date_due, note=""):
        r = Reminder(title, date_due, note)
        self.reminders.append(r)
        return r
    
    def list_overdue(self):
        return [r for r in self.reminders if r.is_overdue() and not r.done]
    
    def mark_done(self, title):
        for r in self.reminders:
            if r.title == title:
                r.done = True
                return f"Напоминание '{title}' отмечено как выполненное."
        return "Напоминание не найдено."

# Пример использования:
rm = ReminderManager()
rm.add("Прочитать главу 5", "2024-12-31")
rm.add("Сдать рецензию", "2025-01-15", "Обсудить с коллегами")
print(rm.list_overdue())
