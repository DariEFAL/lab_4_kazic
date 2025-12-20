import pytest
from fibo_factorial import factorial, factorial_recursive, fibo, fibo_recursive

def test_factorial_basic():
    """Тест базовых случаев факториала"""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(5) == 120
    assert factorial(7) == 5040

def test_factorial_large():
    """Тест на большом числе"""
    assert factorial(10) == 3628800

def test_factorial_recursive_basic():
    """Тест базовых случаев факториала черех рекурсию"""
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(2) == 2
    assert factorial_recursive(3) == 6
    assert factorial_recursive(5) == 120
    assert factorial_recursive(7) == 5040

def test_factorial_recursive_large():
    """Тест на большом числе"""
    assert factorial_recursive(10) == 3628800

def test_fibo_basic():
    """Тест базовых случаев чисел Фибоначчи"""
    assert fibo(0) == 0
    assert fibo(1) == 1 
    assert fibo(2) == 1
    assert fibo(3) == 2
    assert fibo(4) == 3
    assert fibo(5) == 5
    assert fibo(6) == 8 
    assert fibo(7) == 13

def test_fibo_large():
    """Тест на большом числе"""
    assert fibo(10) == 55
    assert fibo(15) == 610
    assert fibo(20) == 6765

def test_fibo_recursive_basic():
    """Тест базовых случаев рекурсивного Фибоначчи"""
    assert fibo_recursive(0) == 0
    assert fibo_recursive(1) == 1
    assert fibo_recursive(2) == 1
    assert fibo_recursive(3) == 2
    assert fibo_recursive(5) == 5
    assert fibo_recursive(8) == 21

def test_fibo_recursive_large():
    """Тест на больших числах"""
    assert fibo_recursive(10) == 55
    assert fibo_recursive(15) == 610
