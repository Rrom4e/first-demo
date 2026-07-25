# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: BookTrail
class UserProfile:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.read_count = 0
        self.avg_rating = 0.0
    
    def add_book(self, rating=None):
        self.read_count += 1
        if rating is not None:
            self.avg_rating = (self.avg_rating * (self.read_count - 1) + rating) / self.read_count

class MultiUserTracker(BaseBookTracker):
    def __init__(self, default_user_id=0, default_username="Guest"):
        super().__init__()
        self._profiles = {default_user_id: UserProfile(default_user_id, default_username)}
    
    def get_profile(self, user_id):
        if user_id not in self._profiles:
            username = input(f"Имя пользователя (user #{user_id}): ")
            self._profiles[user_id] = UserProfile(user_id, username)
        return self._profiles[user_id]
    
    def add_book_for_user(self, book, rating=None):
        profile = self.get_profile(book.user_id if hasattr(book, 'user_id') else 0)
        super().add_book(book, rating)
        if rating is not None:
            profile.add_book(rating)
