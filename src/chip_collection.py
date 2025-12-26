from typing import Iterator, Tuple
from chip_collection import ChipCollection

class ChipCollection:
    def __init__(self, chip_1: int = 0, chip_5: int = 0, chip_25: int = 0, chip_100: int = 0):
        """Инициализация фишек"""
        self.chips = [chip_1, chip_5, chip_25, chip_100]

    def __repr__(self):
        return f"ChipCollection(chip_1={self.chips[0]}, chip_5={self.chips[1]}, chip_25={self.chips[2]}, chip_100={self.chips[3]})"
    
    def __str__(self):
        return f"Фишки: {self.chips[0]}×1$, {self.chips[1]}×5$, {self.chips[2]}×25$, {self.chips[3]}×100$"

    def __iter__(self) -> Iterator[Tuple[int, int]]:
        """"Итерация"""
        nominal = [1, 5, 25, 100]
        for i in range(4):
            yield (self.chips[i], nominal[i])

    def __getitem__(self, key) -> str | int | list[int]:
        """Обращение по индексу и срезы"""
        try:
            return self.chips[key]
        except IndexError:
            return IndexError("IndexError: индекс вне диапозона 0-3")
        
    def __len__(self) -> int:
        """"Нахождение длины. Обращаться len(obj)"""
        return 4
    
    def __iadd__(self, other) -> ChipCollection:
        """Добавление фишек. Обращаться +="""
        self.chips[0] += other.chips[0]
        self.chips[1] += other.chips[1]
        self.chips[2] += other.chips[2]
        self.chips[3] += other.chips[3]
        return self
    
    def __imul__(self, num) -> ChipCollection:
        """Увеличение фишек в num раз. Обращаться *="""
        self.chips[0] *= num
        self.chips[1] *= num
        self.chips[2] *= num
        self.chips[3] *= num
        return self
    
    def __isub__(self, other) -> ChipCollection:
        """Удаление фишек. Обращаться -="""
        self.chips[0] -= other.chips[0]
        self.chips[1] -= other.chips[1]
        self.chips[2] -= other.chips[2]
        self.chips[3] -= other.chips[3]
        return self

    def __ge__(self, other) -> bool:
        """"Сравнение фишек. Обращаться >="""
        return all([self.chips[i] >= other.chips[i] for i in range(4)])
    