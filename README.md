# Лаба 4: Гуси и казино

## Запуск программы
```powershell
 git clone https://github.com/DariEFAL/lab_4_kazic.git
 cd lab_4_kazic
 uv venv
 .venv\Scripts\activate
 (Для Linux: source .venv/bin/activate)
 Установка зависимостей:
 uv pip install -e .
 python src\main.py --steps=20 --seed=3
 Вызов тестов: 
 pytest tests -v
```
