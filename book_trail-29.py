# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: BookTrail
# BookTrail — Этап 30: Конфигурация через словарь настроек
DEFAULT_CONFIG = {
    "max_rating": 5,
    "show_stats_interval": 10,
    "default_page_count": None,
    "allowed_extensions": [".txt", ".pdf", ".epub"],
}

def load_config(path=None):
    if path is None:
        return DEFAULT_CONFIG.copy()
    config = DEFAULT_CONFIG.copy()
    try:
        with open(path) as f:
            user_conf = eval(f.read())
        config.update(user_conf)
    except Exception:
        pass
    return config

def save_config(config, path=None):
    if path is None:
        import tempfile; path = tempfile.mktemp(".conf")
    with open(path, "w") as f:
        f.write(str(config))
