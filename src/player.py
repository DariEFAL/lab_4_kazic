import random

from chip_collection import ChipCollection

class Player:
    def __init__(self, name: str, balance: int = 25):
        """Деньги в долларах. Инициализация игрока"""
        self.name = name
        self.current_balance = balance # Количество денег, без фишек
        self.chips = ChipCollection() #Списковая коллекция фишек
        self.panic = 0 # max = 100
    
    def __repr__(self) -> str:
        return f"Player(name={self.name!r}, balance={self.current_balance}"
    
    def __str__(self) -> str:
        return (f"Игрок: {self.name}\n"
                f"Баланс: ${self.current_balance}\n"
                f"{self.chips}\n"
                f"Уровень паники: {self.panic} из 100")
    
    def buy_chips(self, chip_1: int = 0, chip_5: int = 0, chip_25: int = 0, chip_100: int = 0) -> str:
        """"Покупка/докупка фишек"""
        if chip_1 + chip_5 * 5 + chip_25 * 25 + chip_100 * 100 > self.current_balance:
            return f"""{self.name} имеет недостаточно денег (${self.current_balance}) для покупки фишек {chip_1}x1$, {chip_5}x5$, {chip_25}x25$, {chip_100}x100$."""
        
        self.chips += ChipCollection(chip_1, chip_5, chip_25, chip_100)
        self.current_balance -= chip_1 + chip_5 * 5 + chip_25 * 25 + chip_100 * 100

        return f"""{self.name} купил фишки: {chip_1}x1$, {chip_5}x5$, {chip_25}x25$, {chip_100}x100$."""
    
    def rulette(self, chip_1: int = 0, chip_5: int = 0, chip_25: int = 0, chip_100: int = 0) -> str:
        """Крутить колесо фортуны (10 секций. в 1 - 3x, в 4 - 2x, в 5 - 0x) на какое-то кол-во фишек"""
        bet = ChipCollection(chip_1, chip_5, chip_25, chip_100)

        if chip_1 + chip_5 + chip_25 + chip_100 == 0:
            return f"""{self.name}, нельзя поставить 0 фишек. Ваши фишки: {self.chips[0]}x1$, {self.chips[1]}x5$, {self.chips[2]}x25$, {self.chips[3]}x100$."""
        if not (self.chips >= bet):
            return f"""{self.name}, нельзя поставить несуществующие фишки. Ваши фишки: {self.chips[0]}x1$, {self.chips[1]}x5$, {self.chips[2]}x25$, {self.chips[3]}x100$."""
        
        self.chips -= bet

        print(f"{self.name} крутит колесо фортуны. Ставка {bet[0]}x1$, {bet[1]}x5$, {bet[2]}x25$, {bet[3]}x100$....")

        wheel = [3, 0, 2, 0, 2, 0, 2, 0, 2, 0]
        result = random.choice(wheel)

        bet *= result
        self.chips += bet

        return "    Проигрыш!!!" if result == 0 else f"    Победа!!! Ваши ставка увеличевается в {result} раз"
    
    def transfer_money(self, chip_1: int = 0, chip_5: int = 0, chip_25: int = 0, chip_100: int = 0) -> str:
        """Перевод из фишек в деньги"""
        chip_for_transfer = ChipCollection(chip_1, chip_5, chip_25, chip_100)

        if not (self.chips >= chip_for_transfer):
            return f"""{self.name} имеет недостаточно фишек для перевода в деньги. Ваши фишки: {self.chips[0]}x1$, {self.chips[1]}x5$, {self.chips[2]}x25$, {self.chips[3]}x100$."""
        
        self.chips -= chip_for_transfer
        for count, nominal in chip_for_transfer:
            self.current_balance += count * nominal
        
        return f"""{self.name} перевел фишки: {chip_1}x1$, {chip_5}x5$, {chip_25}x25$, {chip_100}x100$ - в деньги."""
    
