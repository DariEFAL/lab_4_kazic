import typer
from typing import Optional, List
import ast

from const import ALL_FUNCTION, TYPE_T
from fibo_factorial import factorial, factorial_recursive, fibo, fibo_recursive
from sorted import heap_sort, quick_sort, radix_sort, bubble_sort, bucket_sort, counting_sort
from stack_list import Stack
from queue_list import Queue
from benchmark import timeit_once, benchmark_sorts
from test_keys import rand_float_array, rand_int_array, reverse_sorted, many_duplicates, nearly_sorted


app = typer.Typer()

@app.command("factorial")
def cmd_factorial(n: int, recursive: bool = False) -> None:
    """Вызов функций факториала"""
    try:
        if n < 0:
            raise ValueError("Нельзя получить факториал от отрицательного числа")
        
        if recursive:
            typer.echo(factorial_recursive(n))
        else:
            typer.echo(factorial(n))

    except ValueError as e:
        typer.echo(f"ValueError: {e}")
    except Exception as e:
        typer.echo(f"Неожиданная ошибка: {e}")

@app.command("fibo")
def cmd_fibo(n: int, recursive: bool = False) -> None:
    """Вызов функций фибоначи"""
    try:
        if n < 0:
            raise ValueError("Нельзя получить число фибоначи от отрицательного числа")
        
        if recursive:
            typer.echo(fibo_recursive(n))
        else:
            typer.echo(fibo(n))

    except ValueError as e:
        typer.echo(f"ValueError: {e}")
    except Exception as e:
        typer.echo(f"Неожиданная ошибка: {e}")

@app.command("sort_heap")
def cmd_heap_sort(n: Optional[List[str]] = typer.Argument(None)) -> None:
    """Вызов sort_heap"""
    if n is None:
        n = []
    n = list(map(int, n))
    typer.echo(heap_sort(n))

@app.command("sort_quick")
def cmd_quick_sort(n: Optional[List[str]] = typer.Argument(None)) -> None:
    """Вызов sort_quick"""
    if n is None:
        n = []
    n = list(map(int, n))
    typer.echo(quick_sort(n))

@app.command("sort_radix")
def cmd_radix_sort(base: int = 10, n: Optional[List[str]] = typer.Argument(None)) -> None:
    """Вызов sort_radix"""
    if n is None:
        n = []
    n = list(map(int, n))
    typer.echo(radix_sort(n, base))

@app.command("sort_bubble")
def cmd_bubble_sort(n: Optional[List[int]] = typer.Argument(None)) -> None:
    """Вызов sort_bubble"""
    if n is None:
        n = []
    n = list(map(int, n))
    typer.echo(bubble_sort(n))

@app.command("sort_bucket")
def cmd_bucket_sort(buckets: int | None = None, n: Optional[List[float]] = typer.Argument(None)) -> None:
    """Вызов sort_bucket"""
    if n is None:
        n = []
    n = list(map(float, n))
    typer.echo(bucket_sort(n, buckets))

@app.command("sort_counting")
def cmd_сounting_sort(n: Optional[List[int]] = typer.Argument(None)) -> None:
    """Вызов sort_counting"""
    if n is None:
        n = []
    n = list(map(int, n))
    typer.echo(counting_sort(n))

@app.command("rand_float")
def cmd_rand_float(n: int, lo: float = typer.Option(0.0), hi: float = typer.Option(1.0), seed: Optional[int] = typer.Option(None)) -> None:
    """Вызов rand_float_array"""
    try:
        user_input = typer.prompt("Выберите вывод: 1-списком 2-через пробел")

        if user_input == "1":
            print(rand_float_array(n, lo, hi, seed=seed))
        elif user_input == "2":
            print(*rand_float_array(n, lo, hi, seed=seed))
        else:
            raise ValueError(f"'Выберите вывод: 1-списком 2-через пробел' не имеет опции {user_input}")
        
    except ValueError as e:
        typer.echo(f"ValueError: {e}")

@app.command("rand_int")
def cmd_rand_int(n: int, lo: int, hi: int, distinct: bool = False, seed: Optional[int] = typer.Option(None)) -> None:
    """Вызов rand_int_array"""
    try:
        user_input = typer.prompt("Выберите вывод: 1-списком 2-через пробел")

        if user_input == "1":
            print(rand_int_array(n, lo, hi, distinct=distinct, seed=seed))
        elif user_input == "2":
            print(*rand_int_array(n, lo, hi, distinct=distinct, seed=seed))
        else:
            raise ValueError(f"'Выберите вывод: 1-списком 2-через пробел' не имеет опции {user_input}")
        
    except ValueError as e:
        typer.echo(f"ValueError: {e}")

@app.command("reverse_sorted")
def cmd_reverse_sorted(n: int) -> None:
    """Вызов reverse_sorted"""
    try:
        user_input = typer.prompt("Выберите вывод: 1-списком 2-через пробел")

        if user_input == "1":
            print(reverse_sorted(n))
        elif user_input == "2":
            print(*reverse_sorted(n))
        else:
            raise ValueError(f"'Выберите вывод: 1-списком 2-через пробел' не имеет опции {user_input}")
        
    except ValueError as e:
        typer.echo(f"ValueError: {e}")
    
@app.command("many_duplicates")
def cmd_many_duplicates(n: int, k_unique: int = typer.Option(5), seed: Optional[int] = typer.Option(None)) -> None:
    """Вызов many_duplicates"""
    try:
        user_input = typer.prompt("Выберите вывод: 1-списком 2-через пробел")

        if user_input == "1":
            print(many_duplicates(n, k_unique, seed=seed))
        elif user_input == "2":
            print(*many_duplicates(n, k_unique, seed=seed))
        else:
            raise ValueError(f"'Выберите вывод: 1-списком 2-через пробел' не имеет опции {user_input}")
        
    except ValueError as e:
        typer.echo(f"ValueError: {e}")

@app.command("nearly_sorted")
def nearly_sorted(n: int, swaps: int, seed: Optional[int] = typer.Option(None)) -> None:
    """Вызов nearly_sorted"""
    try:
        user_input = typer.prompt("Выберите вывод: 1-списком 2-через пробел")

        if user_input == "1":
            print(nearly_sorted(n, swaps, seed=seed))
        elif user_input == "2":
            print(*nearly_sorted(n, swaps, seed=seed))
        else:
            raise ValueError(f"'Выберите вывод: 1-списком 2-через пробел' не имеет опции {user_input}")
        
    except ValueError as e:
        typer.echo(f"ValueError: {e}")

@app.command("stack")
def cmd_stack() -> None:
    """Интерактивный режим работы со стеком"""
    t = typer.prompt("Введите тип, с которым вы хотите работать в стеке (int, float, str)").strip()

    if t not in TYPE_T:
        raise ValueError(f"Тип {t} не поддерживается")
    
    t = TYPE_T[t]
    st = Stack[t](t)

    typer.echo("=== Интерактивный режим стека ===")
    typer.echo("Доступные команды:")
    typer.echo("  push - добавить элемент")
    typer.echo("  pop - удалить и получить последний элемент")
    typer.echo("  peek - посмотреть последний элемент")
    typer.echo("  min - получить минимальный элемент")
    typer.echo("  size - размер стека")
    typer.echo("  empty - проверка на пустоту")
    typer.echo("  exit - выход")
    typer.echo("================================")

    while True:
        try:
            user_input = typer.prompt(f"stack({t.__name__})>").strip()

            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()

            if command == "exit":
                typer.echo("Выход из режима стека")
                break

            elif command == "push":
                if len(parts) != 2:
                    raise ValueError("Неправильный ввод команды push")

                value = parts[1]

                try:
                    if st.stack_type == str:
                        raise Exception
                    
                    value = float(value)
                    if int(value) == value:
                        value = int(value)
                except Exception:
                    pass

                if not isinstance(value, st.stack_type):
                    raise ValueError(f"Значение {value} не может быть добавлено в стек типа {st.stack_type}")
                
                st.push(value)

            elif command == "pop":
                typer.echo(st.pop())

            elif command == "peek":
                value = st.peek()
                typer.echo(f"Последний элемент: {value}")

            elif command == "empty":
                value = st.is_empty()
                typer.echo(f"Проверка на пустоту: {value}")

            elif command == "min":
                value = st.min()
                typer.echo(f"Минимальный элемент: {value}")

            elif command == "size":
                typer.echo(f"Размер стека: {st.__len__()}")

            else:
                typer.echo(f"Неизвестная команда: {command}")

        except ValueError as e:
            typer.echo(f"ValueError: {e}")
        except IndexError as e:
            typer.echo(f"IndexError: {e}")
        except Exception as e:
            typer.echo(f"Неожиданная ошибка: {e}")

@app.command("queue")
def cmd_queue() -> None:
    """Интерактивный режим работы с очередью"""
    t = typer.prompt("Введите тип, с которым вы хотите работать в очереди (int, float, str)")

    if t not in TYPE_T:
        raise ValueError(f"Тип {t} не поддерживается")
    
    t = TYPE_T[t]
    qu = Queue[t](t)

    typer.echo("=== Интерактивный режим очереди ===")
    typer.echo("Доступные команды:")
    typer.echo("  enqueue - Добавляет элемент в конец очереди")
    typer.echo("  dequeue - Удаляет и возвращает первый элемент очереди")
    typer.echo("  front - Возвращает первый элемент очереди без удаления")
    typer.echo("  size - размер стека")
    typer.echo("  empty - проверка на пустоту")
    typer.echo("  exit - выход")

    typer.echo("================================")

    while True:
        try:
            user_input = typer.prompt(f"queue({t.__name__})>").strip()

            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()

            if command == "exit":
                typer.echo("Выход из режима очереди")
                break

            elif command == "enqueue":
                if len(parts) != 2:
                    raise ValueError("Неправильный ввод")

                value = parts[1]

                try:
                    if qu.queue_type == str:
                        raise Exception
                    
                    value = float(value)
                    if int(value) == value:
                        value = int(value)
                except Exception:
                    pass

                if not isinstance(value, qu.queue_type):
                    raise ValueError(f"Значение {value} не может быть добавлено в очередь типа {qu.queue_type}")
                
                qu.enqueue(value)

            elif command == "dequeue":
                typer.echo(qu.dequeue())

            elif command == "front":
                typer.echo(qu.front())

            elif command == "size":
                typer.echo(f"Размер стека: {qu.__len__()}")

            elif command == "empty":
                typer.echo(f"Проверка на пустоту: {qu.is_empty()}")

            else:
                typer.echo(f"Неизвестная команда: {command}")

        except ValueError as e:
            typer.echo(f"ValueError: {e}")
        except IndexError as e:
            typer.echo(f"IndexError: {e}")
        except Exception as e:
            typer.echo(f"Неожиданная ошибка: {e}")

@app.command("benchmark_once")
def cmd_benchmark_once() -> None:
    """Вызов бенчмарк"""
    try:
        func_name = typer.prompt("Введите имя функции").strip()

        if func_name not in ALL_FUNCTION:
            raise ValueError(f"Функции {func_name} не существует")
        
        func = ALL_FUNCTION[func_name]

        arg = []
        typer.echo("Введите позиционные аргументы каждый раз начиная с новой строки (Список вводить так: [1, 4, 2]). Если закончили введите -")
        while True:
            argument = typer.prompt(">").strip()

            if argument == "-":
                break

            arg.append(ast.literal_eval(argument))

        kwargs = ast.literal_eval(typer.prompt('Введите именнованные аргументы (вводить надо как словарь: {"a": 10, "lo": 10})').strip())
        
        typer.echo(f"Время выполнения {func_name}: {timeit_once(func, *arg, **kwargs):.10f}")

    except ValueError as e:
        typer.echo(f"ValueError: {e}")
    except IndexError as e:
        typer.echo(f"IndexError: {e}")
    except Exception as e:
        typer.echo(f"Неожиданная ошибка: {e}")

@app.command("benchmark_sorted")
def cmd_benchmark_sorted() -> None:
    """Вызов бенчмарк для сравнения алгоритмов сортировок"""
    try:
        algos = {}
        arrays = {}

        typer.echo("Введите каждый раз начиная с новой строки имя функций сортировок, алгоритмы которых хотите сравнить. Если закончили введите -")
        while True:
            func_name = typer.prompt(">").strip()

            if func_name == "-":
                break
            if func_name not in ALL_FUNCTION:
                raise ValueError(f"Функции {func_name} не существует")
            
            algos[func_name] = ALL_FUNCTION[func_name]
        
        typer.echo("Введите каждый раз начиная с новой строки масивы, по которым хотите провести сравнение: [2, 4, 3]. Если закончили введите -")
        while True:
            array = typer.prompt(">").strip()

            if array == "-":
                break

            array_name = typer.prompt("Введите название масива").strip()
            
            arrays[array_name] = ast.literal_eval(array)
        
        result = benchmark_sorts(arrays, algos)

        print(f"{'Названия массива:':<30}", end='')
        for name in algos.keys():
            print(f"{name:<15}", end='')
        print()

        for name_array, alg in result.items():
            print(f"{name_array:<30}", end='')
            for res in alg.values():
                print(f"{res:<15.10f}", end='')
            print()

    except ValueError as e:
        typer.echo(f"ValueError: {e}")
    except IndexError as e:
        typer.echo(f"IndexError: {e}")
    except Exception as e:
        typer.echo(f"Неожиданная ошибка: {e}")