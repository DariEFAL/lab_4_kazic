def factorial(n: int) -> int:
    if n == 0:
        return 1
    
    a = [1] * n
    for i in range(1, n):
        a[i] = a[i-1] * (i + 1)
    return a[-1]

def factorial_recursive(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n - 1)

def fibo(n: int) -> int:
    if n == 0:
        return 0
    
    a = [1] * n
    for i in range(2, n):
        a[i] = a[i-1] + a[i-2]
    return a[-1]

def fibo_recursive(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibo_recursive(n-1) + fibo_recursive(n-2)
