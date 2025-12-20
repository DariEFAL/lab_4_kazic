# Лаба 3: 

## Запуск программы
```powershell
 git clone https://github.com/DariEFAL/lab_3_algorithm.git
 cd lab_3_algorithm
 uv venv
 .venv\Scripts\Activate.ps1
 (Для Linux: source .venv/bin/activate)
 Установка зависимостей:
 pip install -e .
 python -m src.main функция
 Вызов тестов: 
 pytest tests -v
```
- Чтобы для сортировок ввести отрицательные числа надо написать -- перед вводом списка: python src/main.py sortbubble -- 43 -2 -5 0 5
- Если надо ввести отрицательные числа с именнованными аргументами, то надо вводить так: python src/main.py rand_int --distinct -- 9 -2 10

## Команды
* python src/main.py fibo <число> (--recursive)
* python src/main.py factorial <число> (--recursive)
* python src/main.py sort_heap -- <числа>
* python src/main.py sort_quick -- <числа>
* python src/main.py sort_radix (--base=<число>) -- <числа>
* python src/main.py sort_bubble (--buckets=<число>) -- <числа>
* python src/main.py sort_bucket -- <числа>
* python src/main.py sort_counting -- <числа>
* python src/main.py rand_float (--lo=<число> --hi=<число> --seed=<число>) <число>
* python src/main.py rand_int (--distinct --seed=<число>) -- <число> <число> <число>
* python src/main.py reverse_sorted <число>
* python src/main.py many_duplicates (--k_unique=<число> --seed=<число>) <число>
* python src/main.py nearly_sorted (--seed=<число>) -- <число> <число>
* python src/main.py benchmark_once
* python src/main.py benchmark_sorted

### Есть два интерактивных режима

1. python src/main.py queue
**команды работы с очередью:**
* enqueue <число>
* dequeue
* front
* size
* empty
* exit
2. python src/main.py stack
**команды работы со стеком:**
* push
* pop 
* peek 
* min 
* size
* empty
* exit