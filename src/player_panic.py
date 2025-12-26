from player import Player

class PlayerPanic():
    """
    Пользовательская словарная коллекция для отслеживания паники игроков.
    """
    def __init__(self):
        self.panic_history = {}
    
    def __repr__(self) -> str:
        return f"PlayerPanic(panic_history={self.panic_history})"
    
    def __str__(self) -> str:
        return f"""{self.panic_history}"""
    
    