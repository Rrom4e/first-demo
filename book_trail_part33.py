# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: BookTrail
import time

_UNDO_STACK = []

def undo_last():
    if not _UNDO_STACK:
        print("\n⚠ Нет действий для отката.\n")
        return
    state = _UNDO_STACK.pop()
    for key, value in state.items():
        globals()[key] = value
    print("✅ Действие отменено.")
