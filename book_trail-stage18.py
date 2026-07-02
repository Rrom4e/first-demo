# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: BookTrail
class BookTag:
    def __init__(self, name): self.name = name
    
def add_tag(book_id, tag_name):
    if book_id not in books: return False
    for b in books[book_id]:
        if any(t.name == tag_name for t in b.tags): return True
        b.tags.append(BookTag(tag_name))
        return True
    return False

def remove_tag(book_id, tag_name):
    if book_id not in books: return False
    for b in books[book_id]:
        b.tags = [t for t in b.tags if t.name != tag_name]
        return bool(b.tags) or len(books[book_id]) > 0
    return False
