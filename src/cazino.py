import random
from typing import Optional

from users import UsersCazino
from player import Player
from goose import Goose, HonkGoose, PlayGoose

class Casino:
    """Управляет симуляцией, случайными событиями"""
    def __init__(self):
        self.all_users = UsersCazino()
        self.all_goose = UsersCazino()
        self.goose = []
        self.num_user = 1
        self.num_goose = 1

    def add_player(self, player: Player) -> None:
        """Добавляет игрока в казино."""
        self.all_users["User" + str(self.num_user)] = player
        self.num_user += 1
        print(f"Игрок {player.name} зашел в казино!")
    
    def add_goose(self, goose: Goose) -> None:
        """Добавляет гуся в казино."""
        self.all_goose["Goose" + str(self.num_goose)] = goose
        self.num_goose += 1
        print(f"Гусь {goose.name} добавлен в казино!")
    
    def random_player(self) -> Optional[str]:
        """Возвращает случайного игрока или None."""
        name = list(self.all_users)
        return random.choice(name) if len(self.all_users) else None
    
    def random_goose(self) -> Optional[str]:
        """Возвращает случайного гуся или None."""
        name = list(self.all_goose)
        return random.choice(name) if len(self.all_goose) else None
    
    def perform_random_event(self) -> str:
        """
        Выполняет одно случайное событие в казино.
        Возвращает описание события.
        """
        events = [
            self.event_player_buy_chips,
            self.event_goose_steal_chips,
            self.event_player_buy_chips,
            self.event_goose_steal_money,
            self.event_player_buy_chips,
            self.event_player_bet,
            self.event_honk_goose,
            self.event_player_buy_chips,
            self.event_play_goose,
        ]
        
        event_func = random.choice(events)
        event_func()
    
    def event_goose_steal_chips(self) -> None:
        """Гусь крадет фишки у случайного игрока."""
        try:
            player_id = self.random_player()
            goose: Goose = self.all_goose[self.random_goose()]
            player: Player = self.all_users[player_id]
            
            if goose and player:
                if isinstance(goose, HonkGoose):
                    rand = random.choice([0, 1])
                    if rand:
                        print(goose.steal_chip(player))
                    else: 
                        print(goose.enlarged_steal_chip(player))
                
                else: print(goose.steal_chip(player))

                if player.panic == 100:
                    print(f"Игрок {player.name} очень испугался гусей и сбежал из казино.")

                    if isinstance(goose, PlayGoose):
                        goose.chips += player.chips
                        print(f"Все его фишки достались гусю {goose.name}")
                    
                    del self.all_users[player_id]
                    
            else: print("Нет гусей или игроков для кражи фишек.")
        
        except Exception as e:
            print(f"Ошибка: {e}")
    
    def event_goose_steal_money(self) -> None:
        """Гусь крадет деньги у случайного игрока."""
        try:
            player_id = self.random_player()
            goose: Goose = self.all_goose[self.random_goose()]
            player: Player = self.all_users[player_id]
            
            if goose and player:
                if isinstance(goose, HonkGoose):
                    rand = random.choice(0, 1)
                    if rand:
                        print(goose.steal_money(player))
                    else: 
                        print(goose.enlarged_steal_money(player))
                
                else: print(goose.steal_chip(player))

                if player.panic == 100:
                    print(f"Игрок {player.name} очень испугался гусей и сбежал из казино.")

                    if isinstance(goose, PlayGoose):
                        goose.chips += player.chips
                        print(f"Все его фишки достались гусю {goose.name}")

                    del self.all_users[player_id]

            else: print("Нет гусей или игроков для кражи денег.")
        
        except Exception as e:
            print(f"Ошибка: {e}")
    
    def event_player_bet(self) -> None:
        """Игрок делает ставку в рулетке."""
        try:
            player: Player = self.all_users[self.random_player()]
            
            if player:
                print(player.rulette(random.randint(0, player.chips[0]), random.randint(0, player.chips[1]), random.randint(0, player.chips[2]), random.randint(0, player.chips[3])))

            else: print("Нет игроков.")
        
        except Exception as e:
            print(f"Ошибка: {e}")
    
    def event_honk_goose(self) -> None:
        """Гусь-крикун кричит на игрока."""
        try:
            all_honk_goose = UsersCazino()

            for name, goose in self.all_goose.items():
                if isinstance(goose, HonkGoose):
                    all_honk_goose[name] = goose
            
            goose: HonkGoose = all_honk_goose[random.choice(list(all_honk_goose))]
            player_id = self.random_player()
            player: Player = self.all_users[player_id]

            if goose and player:
                print(goose.honk(player))

                if player.panic == 100:
                    print(f"Игрок {player.name} очень испугался гусей и сбежал из казино.")

                    del self.all_users[player_id]
                    
            else: print("Нет гусей-крикунов")

        except Exception as e:
            print(f"Ошибка: {e}")
    
    def event_play_goose(self) -> None:
        """Гусь-игрок крутить рулетку."""
        try:
            all_play_goose = UsersCazino()

            for name, goose in self.all_goose.items():
                if isinstance(goose, PlayGoose):
                    all_play_goose[name] = goose
            
            goose: PlayGoose = all_play_goose[random.choice(list(all_play_goose))]
            player: Player = self.all_users[self.random_player()]

            if goose and player:
                print(goose.rulette(random.randint(0, player.chips[0]), random.randint(0, player.chips[1]), random.randint(0, player.chips[2]), random.randint(0, player.chips[3])))
                    
            else: print("Нет гусей-игроков")

        except Exception as e:
            print(f"Ошибка: {e}")
    
    def event_player_buy_chips(self) -> None:
        """игрок покупает фишки в казино."""
        try:
            player_id = self.random_player()
            if player_id is None:
                return
            
            player: Player = self.all_users[player_id]

            chip_1 = random.randint(5, 50)
            chip_5 = random.randint(0, 15)
            chip_25 = random.randint(0, 8)
            chip_100 = random.randint(0, 2)
            
            while chip_1 + chip_5 * 5 + chip_25 * 25 + chip_100 * 100 > player.current_balance:
                chip_1 = random.randint(5, 50)
                chip_5 = random.randint(0, 10)
                chip_25 = random.randint(0, 4)
                chip_100 = random.randint(0, 2)
            
            print(player.buy_chips(chip_1, chip_5, chip_25, chip_100))
            
        except Exception as e:
            print(f"Ошибка: {e}")

