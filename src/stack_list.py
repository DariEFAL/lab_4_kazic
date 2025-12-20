from typing import TypeVar, Generic, Optional

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self, stack_type: Optional[type[T]] = None):
        self.stack: list[tuple[T, T]] = []
        self.stack_type: type[T] = stack_type

    def push(self, x: T) -> None:
        """Добавляет элемент в конец стека"""
        if self.is_empty():
            mn_now = x
        else:
            mn_now = min(self.stack[-1][1], x)

        self.stack.append((x, mn_now))

    def pop(self) -> T:
        """Удаляет и возвращает последний элемент стека"""
        if self.is_empty():
            raise IndexError("Пустой стек")

        return self.stack.pop()[0]

    def peek(self) -> T:
        """Возвращает последний элемент стека без удаления"""
        if self.is_empty():
            raise IndexError("Пустой стек")

        return self.stack[-1][0]

    def is_empty(self) -> bool:
        """Проверяет на пустоту"""
        return len(self.stack) == 0

    def __len__(self) -> int:
        """Возвращает количество элементов в стеке"""
        return len(self.stack)

    def min(self) -> T:
        """Возвращает минимальный элемент в стеке"""
        if self.is_empty():
            raise ValueError("Пустой стек")

        return self.stack[-1][1]
