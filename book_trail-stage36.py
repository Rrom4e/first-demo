# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: BookTrail
def check_integrity(data):
    """Checks if all required keys exist in each book record."""
    errors = []
    for i, (title, info) in enumerate(data.items(), 1):
        if not isinstance(info, dict):
            errors.append(f"Book {i} ({title}): value is not a dict")
            continue
        for key in ["pages", "author"]:
            if key not in info:
                errors.append(f"Book {i} ({title}): missing required key '{key}'")
    return errors

def repair_data(data):
    """Replaces missing 'pages' with 0 and missing 'author' with 'Unknown'."""
    repaired = {}
    for i, (title, info) in enumerate(data.items(), 1):
        if not isinstance(info, dict):
            repaired[title] = {"pages": 0, "author": "Unknown"}
            continue
        repaired[title] = {**info}
        if "pages" not in repaired[title]:
            repaired[title]["pages"] = 0
        if "author" not in repaired[title]:
            repaired[title]["author"] = "Unknown"
    return repaired

def run_diagnostics(data):
    """Prints integrity report and auto-repairs bad records."""
    errors = check_integrity(data)
    if errors:
        print(f"[BookTrail] Found {len(errors)} error(s):\n")
        for e in errors:
            print(f"  ✗ {e}")
        repaired = repair_data(data)
        print("\n[BookTrail] Data auto-repaired. Here is the fixed version:\n")
        print(repr(repaired))
    else:
        print("[BookTrail] All data is intact — no action needed.")
