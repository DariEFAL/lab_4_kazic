import typer

import random
from typing import Optional

from cazino import Casino
from player import Player
from goose import Goose, HonkGoose, PlayGoose

app = typer.Typer()

@app.command()
def run_simulation( steps: int = typer.Option(20, "--steps"), seed: Optional[int] = typer.Option(None, "--seed")) -> None:
    """
    Основная функция симуляции казино с гусями.
    """
    if seed is not None:
        random.seed(seed)
        print(f"Установлен seed: {seed}")
    
    print("\n" + "="*60)
    print("ЗАПУСК СИМУЛЯЦИИ КАЗИНО С ГУСЯМИ")
    print("="*60)
    
    casino = Casino()
    
    players = [
        Player("Will", balance=111),
        Player("Hopper", balance=150),
        Player("Lucas", balance=80), 
        Player("Dustin", balance=100),
        Player("Stive", balance=500),
        Player("Nenci", balance=325),
        Player("Mike", balance=210)
    ]
    
    for player in players:
        casino.add_player(player)
    
    geese = [
        HonkGoose("Vecna", 10, 40, 5),
        PlayGoose("Demogorgon"),
        Goose("Demon", 7, 2), 
        Goose("Demon1", 10, 1),
        Goose("Mili", 15, 3),
        PlayGoose("Odi"),
        HonkGoose("W", 6, 35, 4)
    ]
    
    for goose in geese:
        casino.add_goose(goose)
    
    print("\n" + "="*10)
    print("НАЧАЛО СИМУЛЯЦИИ")
    print("="*10)
    print(f"Всего шагов: {steps}")
    print("="*10)
    
    for step in range(1, steps + 1):
        print(f"\n--- Шаг {step} ---")
        
        try:
            casino.perform_random_event()
        except Exception as e:
            print(f"Ошибка на шаге {step}: {e}")
        
        if step % 5 == 0:
            print(f"\nПРОМЕЖУТОЧНАЯ СТАТИСТИКА (шаг {step})")
            print("-" * 10)
            
            print("Игроки:")
            for player in casino.all_users.values():
                print(f"  {player.name}: Баланс ${player.current_balance}, "
                      f"{player.chips}, Паника: {player.panic}")

            print("-" * 10)
            print(f"КОНЕЦ ПРОМЕЖУТОЧНОЙ СТАТИСТИКИ (шаг {step})")
        
    print("\n" + "="*10)
    print("КОНЕЦ СИМУЛЯЦИИ")