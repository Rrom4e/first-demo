# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: BookTrail
class DryRunError(Exception):
    """Raised when a dry-run operation is executed instead of the real one."""
    pass

class DryRunContext:
    """Context manager that records operations instead of executing them."""
    def __init__(self):
        self.operations = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self._print_summary()
        return False

    def _print_summary(self):
        if not self.operations:
            print("Dry-run: no operations recorded.")
            return
        print("Dry-run summary:")
        for op in self.operations:
            print(f"  - {op}")

    def record(self, op):
        self.operations.append(op)

class DryRunTracker(BookTracker):
    def __init__(self, dry_run=False):
        super().__init__()
        self._dry_run = dry_run
        if dry_run:
            self._ctx = DryRunContext()

    def _execute(self, action, *args, **kwargs):
        if self._dry_run:
            self._ctx.record(f"[DRY-RUN] {action} {args}")
            return None
        return action(*args, **kwargs)

    def add_book(self, title, author, **kwargs):
        return self._execute("add_book", title, author, **kwargs)

    def add_progress(self, book_id, page, **kwargs):
        return self._execute("add_progress", book_id, page, **kwargs)

    def add_quote(self, book_id, text, page=None, **kwargs):
        return self._execute("add_quote", book_id, text, page=page, **kwargs)

    def rate_book(self, book_id, rating, **kwargs):
        return self._execute("rate_book", book_id, rating, **kwargs)

    def get_book(self, book_id):
        return self._execute("get_book", book_id)

    def get_progress(self, book_id):
        return self._execute("get_progress", book_id)

    def get_quotes(self, book_id):
        return self._execute("get_quotes", book_id)

    def get_ratings(self, book_id):
        return self._execute("get_ratings", book_id)

    def get_summary(self):
        return self._execute("get_summary")

    def get_stats(self):
        return self._execute("get_stats")
