from typing import TypeVar, Generic, Optional

T = TypeVar("T")

class Queue(Generic[T]):
    def __init__(self, queue_type: Optional[type[T]] = None):
        self.queue: list[T] = []
        self.queue_type: type[T] = queue_type

    def enqueue(self, x: T) -> None:
        """Добавляет элемент в конец очереди"""
        self.queue.append(x)

    def dequeue(self) -> T:
        """Удаляет и возвращает первый элемент очереди"""
        if self.is_empty():
            raise IndexError("Пустая очередь")

        return self.queue.pop(0)

    def front(self) -> T:
        """Возвращает первый элемент очереди без удаления"""
        if self.is_empty():
            raise IndexError("Пустая очередь")

        return self.queue[0]

    def is_empty(self) -> bool:
        """Проверяет на пустоту"""
        return len(self.queue) == 0

    def __len__(self) -> int:
        """Возвращает количество элементов в очереди"""
        return len(self.queue)
