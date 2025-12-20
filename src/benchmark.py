import time
from typing import Dict, List, Callable

from fibo_factorial import factorial, factorial_recursive, fibo, fibo_recursive
from sorted import heap_sort, quick_sort, radix_sort, bubble_sort, bucket_sort, counting_sort

def timeit_once(func: Callable, *args, **kwargs) -> float:
    """Измеряет время выполнения функции один раз"""
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()

    return end_time - start_time


def benchmark_sorts(arrays: Dict[str, List[int]], algos: Dict[str, Callable]) -> Dict[str, Dict[str, float]]:
    """Сравнивает несколько алгоритмов на нескольких массивах"""
    result = {}

    for arrays_name, arrays_list in arrays.items():
        result[arrays_name] = {}

        for algos_name, algos_func in algos.items():
            result[arrays_name][algos_name] = timeit_once(algos_func, arrays_list)

    return result

