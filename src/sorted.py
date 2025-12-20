def bubble_sort(a: list[int]) -> list[int]:
    a = a[:]
    swapped = False
    l_a = len(a)

    for i in range(l_a - 1):
        for j in range(l_a - 1 - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True

        if not swapped:
            return a

    return a


def quick_sort(n: list[int | float]) -> list[int | float]:
    if len(n) <= 1:
        return n[:]

    pivot = n[len(n) // 2]
    left = [i for i in n if i < pivot]
    middle = [i for i in n if i == pivot]
    right = [i for i in n if i > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def counting_sort(n: list[int]) -> list[int]:
    if len(n) <= 1:
        return n[:]

    mn = min(n)
    mx = max(n)
    shift = 0
    if mn < 0:
        shift = -1 * mn

    n_count = [0] * (mx + 1 + shift)
    for i in n:
        n_count[i + shift] += 1

    result = []
    for i, count in enumerate(n_count):
        result.extend([i - shift] * count)

    return result


def radix_sort(n: list[int], base: int = 10) -> list[int]:
    if len(n) <= 1:
        return n[:]

    mn = min(n)
    shift = 0
    if mn < 0:
        shift = -1 * mn
    n = [i + shift for i in n]

    mx_digit = max(len(str(i)) for i in n)
    arr = [[] for i in range(base)]

    for i in range(0, mx_digit):
        for j in n:
            digit = (j // 10 ** i) % base
            arr[digit].append(j)

        n = [y for x in arr for y in x]
        arr = [[] for i in range(base)]

    return [i - shift for i in n]


def bucket_sort(n: list[float], buckets: int | None = None) -> list[float]:
    if len(n) <= 1:
        return n[:]

    if buckets is None:
        buckets = len(n)

    mn = min(n)
    mx = max(n)
    if mn == mx:
        return n[:]

    bucket_width = (mx - mn) / buckets
    bucket_list = [[] for i in range(buckets)]

    for x in n:
        i = int((x - mn) / bucket_width)

        if i == buckets:
            i -= 1

        bucket_list[i].append(x)

    for i in range(buckets):
        bucket_list[i] = quick_sort(bucket_list[i])

    result = []
    for i in bucket_list:
        result.extend(i)

    return result


def heapify(arr: list[int], len_arr, i) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len_arr and arr[left] > arr[i]:
        largest = left

    if right < len_arr and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, len_arr, largest)

def heap_sort(n: list[int]) -> list[int]:
    arr = n[:]
    len_arr = len(arr)

    for i in range(len_arr//2 -1, -1, -1):
        heapify(arr, len_arr, i)

    for i in range(len_arr-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr
