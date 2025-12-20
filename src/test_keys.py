import random

def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    """Создаёт массив из n случайных целых чисел в диапазоне lo-hi"""
    rand = random.Random(seed) if seed is not None else random.Random()

    if distinct:
        if (hi - lo + 1) < n:
            raise ValueError(f"Невозможно сделать {n} уникальных чисел в диапозона {lo}-{hi} ")
        
        return rand.sample(range(lo, hi + 1), n)
    
    return [rand.randint(lo, hi) for i in range(n)]


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    """Создаёт почти отсортированный массив длины n"""
    rand = random.Random(seed) if seed is not None else random.Random()

    lst = list(range(n))

    for k in range(swaps):
        i = rand.randint(0, n - 1)
        j = rand.randint(0, n - 1)
        lst[i], lst[j] = lst[j], lst[i]
    
    return lst


def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    """Создаёт массив длины n, но только из k_unique уникальных чисел"""
    if n < k_unique:
        raise ValueError(f"Невозможно выбрать {k_unique} уникальных элементов из {n}")
    
    rand = random.Random(seed) if seed is not None else random.Random()

    lst_unique = list(range(k_unique))

    return [rand.choice(lst_unique) for i in range(n)]


def reverse_sorted(n: int) -> list[int]:
    """Создаёт массив, отсортированный в обратном порядке"""
    return list(range(n, 0, -1))


def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    """Создаёт массив случайных дробных чисел в диапазоне lo-hi"""
    rand = random.Random(seed) if seed is not None else random.Random()

    return [rand.uniform(lo, hi) for i in range(n)]