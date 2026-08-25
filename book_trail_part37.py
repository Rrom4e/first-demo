# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: BookTrail
import unittest

class TestBookTrail(unittest.TestCase):
    def test_add_book(self):
        from booktrail import BookTrail
        trail = BookTrail()
        trail.add_book("1984", "Оруэлл")
        books = trail.get_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "1984")

    def test_mark_page(self):
        from booktrail import BookTrail
        trail = BookTrail()
        trail.add_book("1984", "Оруэлл")
        trail.mark_page("1984", 50)
        page = trail.get_page("1984")
        self.assertEqual(page, 50)

    def test_rate_book(self):
        from booktrail import BookTrail
        trail = BookTrail()
        trail.add_book("1984", "Оруэлл")
        trail.rate_book("1984", 5)
        rating = trail.get_rating("1984")
        self.assertEqual(rating, 5)

    def test_get_progress(self):
        from booktrail import BookTrail
        trail = BookTrail()
        trail.add_book("1984", "Оруэлл")
        trail.mark_page("1984", 100)
        trail.rate_book("1984", 4)
        progress = trail.get_progress("1984")
        self.assertEqual(progress, 100)

    def test_add_quote(self):
        from booktrail import BookTrail
        trail = BookTrail()
        trail.add_book("1984", "Оруэлл")
        trail.add_quote("1984", "War is peace.")
        quotes = trail.get_quotes("1984")
        self.assertEqual(len(quotes), 1)
        self.assertEqual(quotes[0], "War is peace.")

    def test_get_stats(self):
        from booktrail import BookTrail
        trail = BookTrail()
        trail.add_book("1984", "Оруэлл")
        trail.add_book("Animal Farm", "Оруэлл")
        trail.mark_page("1984", 100)
        trail.mark_page("Animal Farm", 80)
        trail.rate_book("1984", 5)
        trail.rate_book("Animal Farm", 4)
        stats = trail.get_stats()
        self.assertEqual(stats["total_books"], 2)
        self.assertEqual(stats["total_pages"], 180)
        self.assertEqual(stats["total_rating"], 9)
        self.assertEqual(stats["avg_rating"], 4.5)

if __name__ == "__main__":
    unittest.main()
