# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: BookTrail
class ProfileManager:
    def __init__(self):
        self.profiles = {}
        self.active_profile_name = None
    
    def add_profile(self, name, preferences=None):
        if not name or name in self.profiles:
            return False
        self.profiles[name] = {'preferences': preferences or {}}
        self.active_profile_name = name
        return True
    
    def set_active_profile(self, profile_name):
        if profile_name and profile_name in self.profiles:
            self.active_profile_name = profile_name
            return True
        return False
    
    def get_active_profile(self):
        return self.active_profile_name
    
    def delete_profile(self, profile_name):
        if profile_name != self.active_profile_name:
            del self.profiles[profile_name]
            return True
        return False
    
    def list_profiles(self):
        return dict(sorted(self.profiles.items()))
