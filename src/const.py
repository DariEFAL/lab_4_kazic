from typing import Callable

from fibo_factorial import factorial, factorial_recursive, fibo, fibo_recursive
from sorted import heap_sort, quick_sort, radix_sort, bubble_sort, bucket_sort, counting_sort


ALL_FUNCTION: dict[str, Callable] = {
    "fibo": fibo,
    "fibo_r": fibo_recursive,
    "factorial": factorial,
    "factorial_r": factorial_recursive,
    "sort_heap": heap_sort,
    "sort_quick": quick_sort,
    "sort_radix": radix_sort,
    "sort_bubble": bubble_sort,
    "sort_bucket": bucket_sort,
    "sort_counting": counting_sort,
}

TYPE_T: dict[str, type] = {
    "int": int,
    "float": float,
    "str": str,
}