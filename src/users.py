

class UsersCazino():
    """
    Пользовательская словарная коллекция для отслеживания всех пользователей казино.
    """
    def __init__(self):
        self.users = {}
        
    def __repr__(self) -> str:
        return f"UsersCazino(panic_history={self.users})"
    
    def __str__(self) -> str:
        return f"""{self.users}"""
    
    def __iter__(self) -> str:
        """"Итерация"""
        return iter(self.users.keys())

    def __getitem__(self, key):
        """Позволяет обращаться через self[key]"""
        return self.users[key]
    
    def __setitem__(self, key, value):
        """Позволяет делать self[key] = value"""
        self.users[key] = value
    
    def __delitem__(self, key):
        """Позволяет удалять через del self[key]"""
        del self.users[key]
    
    def __contains__(self, key):
        """Позволяет проверять через 'key in self'"""
        return key in self.users
    
    def __len__(self):
        """Позволяет использовать len(self)"""
        return len(self.users)
    
    def keys(self):
        """Возвращает ключи"""
        return self.users.keys()
    
    def values(self):
        """Возвращает значения"""
        return self.users.values()
    
    def items(self):
        """Возвращает пары ключ-значение"""
        return self.users.items()
    
    
