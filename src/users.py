from __future__ import annotations
from typing import Iterator, Iterable, Tuple
from player import Player
from goose import Goose

class UsersCazino():
    """
    Пользовательская словарная коллекция для отслеживания всех пользователей казино.
    """
    def __init__(self):
        self.users = {}
        
    def __repr__(self) -> str:
        return f"UsersCazino(users={self.users})"
    
    def __str__(self) -> str:
        return f"""{self.users}"""
    
    def __iter__(self) -> Iterator[str]:
        """"Итерация"""
        return iter(self.users.keys())

    def __getitem__(self, key) -> Player | Goose | None:
        """Позволяет обращаться через self[key]"""
        return self.users[key]
    
    def __setitem__(self, key, value) -> None:
        """Позволяет делать self[key] = value"""
        self.users[key] = value
    
    def __delitem__(self, key) -> None:
        """Позволяет удалять через del self[key]"""
        del self.users[key]
    
    def __contains__(self, key) -> bool:
        """Позволяет проверять через 'key in self'"""
        return key in self.users
    
    def __len__(self) -> int:
        """Позволяет использовать len(self)"""
        return len(self.users)
    
    def __add__(self, other: UsersCazino) -> UsersCazino:
        """Объединение двух коллекций UsersCazino."""
        
        result = UsersCazino()
        result.users.update(self.users)
        result.users.update(other.users)
        
        return result
    
    def keys(self) -> str:
        """Возвращает ключи"""
        return self.users.keys()
    
    def values(self) -> Player:
        """Возвращает значения"""
        return self.users.values()
    
    def items(self) -> Iterable[Tuple[str, Player]]:
        """Возвращает пары ключ-значение"""
        return self.users.items()
    
    
