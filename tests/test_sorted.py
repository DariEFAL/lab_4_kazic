from sorted import heap_sort, quick_sort, radix_sort, bubble_sort, bucket_sort, counting_sort

import pytest
import random
from sorted import bubble_sort, quick_sort, counting_sort, radix_sort, bucket_sort, heap_sort

def test_all_sorts_empty_list():
    """Все сортировки должны корректно обрабатывать пустой список"""
    assert bubble_sort([]) == []
    assert quick_sort([]) == []
    assert counting_sort([]) == []
    assert radix_sort([]) == []
    assert bucket_sort([]) == []
    assert heap_sort([]) == []

def test_all_sorts_single_element():
    """Сортировка списка из одного элемента"""
    assert bubble_sort([42]) == [42]
    assert quick_sort([42]) == [42]
    assert counting_sort([42]) == [42]
    assert radix_sort([42]) == [42]
    assert bucket_sort([0.88]) == [0.88]
    assert heap_sort([42]) == [42]

def test_all_sorts_already_sorted():
    """Уже отсортированный массив"""
    lst = [1, 2, 3, 4, 5]
    for sort_func in [bubble_sort, quick_sort, counting_sort, radix_sort, heap_sort]:
        assert sort_func(lst) == lst
    
    lst = [0.1, 0.2, 0.3, 0.4, 0.5]
    assert bucket_sort(lst) == lst

def test_all_sorts_reverse_sorted():
    """Обратно отсортированный массив"""
    lst = [5, 4, 3, 2, 1]
    
    for sort_func in [bubble_sort, quick_sort, counting_sort, radix_sort, heap_sort]:
        assert sort_func(lst) == sorted(lst)
    
    lst = [5.0, 4.0, 3.0, 2.0, 1.0]
    assert bucket_sort(lst) == sorted(lst)

def test_all_sorts_random():
    """Случайный массив"""
    lst = [-2, -5, -2, 0, 4, 2, 0, -2, 0]
    
    for sort_func in [bubble_sort, quick_sort, counting_sort, radix_sort, heap_sort]:
        assert sort_func(lst) == sorted(lst)
    
    lst = [2.034445074498011, 2.5961634919477588, 2.4431721259070196, 2.541426069839224, 2.324867272564347, 2.2784589388711316, 2.06395808589273, 2.675004948776378, 2.887674063819131, 2.023317890408658]
    assert bucket_sort(lst) == sorted(lst)