# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: BookTrail
import unittest

class TestBookTrailEdgeCases(unittest.TestCase):
    def setUp(self):
        from booktrail import BookTrail
        self.trail = BookTrail()

    def test_add_page_zero(self):
        self.trail.add_book("TestBook")
        for i in range(100):
            self.trail.add_page("TestBook", "chapter1", f"page {i}")

    def test_add_page_negative(self):
        with self.assertRaises(ValueError):
            self.trail.add_page("TestBook", "chapter1", "-1")

    def test_add_page_none(self):
        with self.assertRaises(ValueError):
            self.trail.add_page("TestBook", "chapter1", None)

    def test_add_page_float(self):
        with self.assertRaises(ValueError):
            self.trail.add_page("TestBook", "chapter1", 1.5)

    def test_add_book_none(self):
        with self.assertRaises(ValueError):
            self.trail.add_book(None)

    def test_add_book_empty_string(self):
        with self.assertRaises(ValueError):
            self.trail.add_book("")

    def test_add_page_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.trail.add_page("NonExistentBook", "chapter1", "page 1")

    def test_add_page_nonexistent_chapter(self):
        self.trail.add_book("TestBook")
        with self.assertRaises(ValueError):
            self.trail.add_page("TestBook", "nonexistent_chapter", "page 1")

    def test_add_page_duplicate(self):
        self.trail.add_book("TestBook")
        self.trail.add_page("TestBook", "chapter1", "page 1")
        self.trail.add_page("TestBook", "chapter1", "page 2")

    def test_get_progress_empty(self):
        self.trail.add_book("TestBook")
        progress = self.trail.get_progress("TestBook")
        self.assertEqual(progress["total_pages"], 0)
        self.assertEqual(progress["completed_chapters"], set())

    def test_add_page_empty_string(self):
        with self.assertRaises(ValueError):
            self.trail.add_page("TestBook", "chapter1", "")

    def test_get_progress_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.trail.get_progress("NonExistentBook")

    def test_add_page_empty_chapter(self):
        self.trail.add_book("TestBook")
        with self.assertRaises(ValueError):
            self.trail.add_page("TestBook", "", "page 1")

    def test_add_page_duplicate_page(self):
        self.trail.add_book("TestBook")
        self.trail.add_page("TestBook", "chapter1", "page 1")
        with self.assertRaises(ValueError):
            self.trail.add_page("TestBook", "chapter1", "page 1")

if __name__ == "__main__":
    unittest.main()
