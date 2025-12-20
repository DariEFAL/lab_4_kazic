import pytest
from stack_list import Stack

class TestStackBasic:
    """Базовые тесты для стека"""
    
    def test_empty_stack(self):
        """Тест создания пустого стека"""
        stack = Stack[int](int)
        assert stack.is_empty() == True
        assert len(stack) == 0
        
    def test_push_single(self):
        """Тест добавления одного элемента"""
        stack = Stack[int](int)
        stack.push(10)
        
        assert stack.is_empty() == False
        assert len(stack) == 1
        assert stack.peek() == 10
        
    def test_push_multiple(self):
        """Тест добавления нескольких элементов"""
        stack = Stack[int](int)
        stack.push(10)
        stack.push(20)
        stack.push(30)
        
        assert len(stack) == 3
        assert stack.peek() == 30 
        
    def test_pop_basic(self):
        """Тест удаления элементов"""
        stack = Stack[int](int)
        stack.push(10)
        stack.push(20)
        stack.push(30)
        
        assert stack.pop() == 30
        assert stack.pop() == 20
        assert stack.pop() == 10
        assert stack.is_empty() == True
        
    def test_peek_no_modification(self):
        """Тест, что peek не изменяет стек"""
        stack = Stack[int](int)
        stack.push(10)
        stack.push(20)
        
        start_len = len(stack)
        
        assert stack.peek() == 20
        assert len(stack) == start_len

class TestStackMin:
    """Тесты для min()"""
    
    def test_min_single_element(self):
        """Минимум в стеке из одного элемента"""
        stack = Stack[int](int)
        stack.push(10)
        assert stack.min() == 10
        
    def test_min_multiple_elements(self):
        """Минимум при добавлении элементов в разном порядке"""
        stack = Stack[int](int)
        
        stack.push(5)
        assert stack.min() == 5
        
        stack.push(3)
        assert stack.min() == 3
        
        stack.push(7)
        assert stack.min() == 3
        
        stack.push(1)
        assert stack.min() == 1

class TestStackError:
    """Тесты обработки ошибок"""
    
    def test_pop_empty_stack(self):
        """Попытка удалить из пустого стека"""
        stack = Stack[int](int)
        
        with pytest.raises(IndexError):
            stack.pop()
        
    def test_peek_empty_stack(self):
        """peek к пустому стеку"""
        stack = Stack[int](int)
        
        with pytest.raises(IndexError):
            stack.peek()
        
    def test_min_empty_stack(self):
        """минимум из пустого стека"""
        stack = Stack[int](int)
        
        with pytest.raises(ValueError):
            stack.min()