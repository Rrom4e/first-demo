# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: BookTrail
class BookSearch:
    def __init__(self, books):
        self.books = books
    
    def search(self, query=None):
        if not query:
            return self.books
        
        query_lower = query.lower()
        
        results = []
        for book in self.books:
            title_match = query_lower in book['title'].lower()
            author_match = query_lower in book['author'].lower()
            
            if title_match or author_match:
                results.append(book)
        
        return results
