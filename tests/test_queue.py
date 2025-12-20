import pytest
from queue_list import Queue 

class TestQueueBasic:
    """Базовые тесты для очереди"""
    
    def test_empty_queue(self):
        """Тест создания пустой очереди"""
        queue = Queue[int](int)
        assert queue.is_empty() == True
        assert len(queue) == 0
        
    def test_enqueue_single(self):
        """Тест добавления одного элемента"""
        queue = Queue[int](int)
        queue.enqueue(10)
        
        assert queue.is_empty() == False
        assert len(queue) == 1
        assert queue.front() == 10
        
    def test_enqueue_multiple(self):
        """Тест добавления нескольких элементов"""
        queue = Queue[int](int)
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        
        assert len(queue) == 3
        assert queue.front() == 10 
        
    def test_dequeue_basic(self):
        """Тест удаления элементов"""
        queue = Queue[int](int)
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        
        assert queue.dequeue() == 10 
        assert queue.dequeue() == 20
        assert queue.dequeue() == 30
        assert queue.is_empty() == True
        
    def test_front_no_modification(self):
        """Тест, что front не изменяет очередь"""
        queue = Queue[int](int)
        queue.enqueue(10)
        queue.enqueue(20)
        
        start_len = len(queue)
        
        assert queue.front() == 10
        assert len(queue) == start_len 
        assert queue.dequeue() == 10

class TestQueueError:
    """Тесты обработки ошибок"""
    
    def test_dequeue_empty_queue(self):
        """Попытка удалить из пустой очереди"""
        queue = Queue[int](int)
        
        with pytest.raises(IndexError):
            queue.dequeue()
        
    def test_front_empty_queue(self):
        """front к пустой очереди"""
        queue = Queue[int](int)
        
        with pytest.raises(IndexError):
            queue.front()
   