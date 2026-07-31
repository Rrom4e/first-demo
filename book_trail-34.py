# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: BookTrail
class Template:
    def __init__(self, name, description, author=None):
        self.name = name
        self.description = description
        self.author = author

    def to_dict(self):
        return {"name": self.name, "description": self.description, "author": self.author}


def save_templates(templates_path="templates.json"):
    with open(templates_path, 'w', encoding='utf-8') as f:
        json.dump(templates_list, f, ensure_ascii=False, indent=2)


def load_templates(templates_path="templates.json"):
    if os.path.exists(templates_path):
        with open(templates_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return [Template("Default", "A simple reading template")]


def create_template(name, description="Quick note for a book section"):
    t = Template(name, description)
    templates_list.append(t)
    save_templates()
    print(f"Template '{name}' created!")
