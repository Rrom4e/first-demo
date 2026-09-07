# === Stage 45: Добавь восстановление из резервной копии ===
# Project: BookTrail
import json, os

def restore_backup():
    backup_path = "booktrail_backup.json"
    if not os.path.exists(backup_path):
        print("Резервная копия не найдена.")
        return False
    with open(backup_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            with open("booktrail_data.json", "w", encoding="utf-8") as out:
                json.dump(data, out, ensure_ascii=False, indent=2)
            print("Резервная копия успешно восстановлена.")
            return True
        except Exception as e:
            print(f"Ошибка восстановления: {e}")
            return False
