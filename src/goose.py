import random
from chip_collection import ChipCollection
from player import Player

class Goose:
    def __init__(self, name: str, power: int = 10, steal: int = 2):
        """Инициализация обычного гуся."""
        self.name = name

        if power > 20:
            power = 20
        self.power_panic = power  # Сила гуся, которая влияет на панику игрока

        if steal > 5:
            steal = 5
        self.steal_chips = steal  # Максимальное кол-во фишек, которое гусь может украсть у игрока
    
    def __repr__(self) -> str:
        return f"Goose(name={self.name!r}, power={self.power_panic}, steal={self.steal_chips})"
    
    def __str__(self) -> str:
        return f"Гусь {self.name} (сила паники у игрока после кражи: {self.power_panic}, кража: до {self.steal_chips} фишек)"
    
    def steal_chip(self, player: Player) -> str:
        """Гусь пытается украсть фишки у игрока."""
        print(f"Гусь, {self.name}, бежит на игрока {player.name}!!!")

        if not player.chips.no_zero_chips():
            player.panic = min(100, player.panic + self.power_panic // 2)
            return f"{self.name} пытается украсть у {player.name}, но у того нет фишек!"
        
        random_steal_chips = random.randint(1, self.steal_chips)
        
        stolen = ChipCollection()
        
        while random_steal_chips != 0 and player.chips.no_zero_chips():
            index = random.choice(player.chips.no_zero_chips()) # рандомный индекс для фишек ненулегого количеста
            count_for_steal = random.randint(0, player.chips[index]) # рандомное количесво из выбранных фишек
            stolen[index] += count_for_steal 

            player.chips[index] -= count_for_steal 
            random_steal_chips -= 1

        player.panic = min(100, player.panic + self.power_panic)
        
        if sum(i[0] for i in stolen) > 0:
            stolen_value = sum(i[0] * i[1] for i in stolen)
            
            return (f"{self.name} украл у {player.name}: {stolen[0]}x1$, {stolen[1]}x5$, "
                    f"{stolen[2]}x25$, {stolen[3]}x100$ (${stolen_value}). "
                    f"Паника игрока: {player.panic}")
        else:
            return f"{self.name} не смог ничего украсть у {player.name}!"
    
    def steal_money(self, player: Player) -> str:
        """Гусь пытается украсть наличные деньги у игрока."""
        print(f"Гусь, {self.name}, бежит на игрока {player.name}!!!")

        if player.current_balance == 0:
            player.panic = min(100, player.panic + self.power_panic // 2)
            return f"{self.name} пытается украсть деньги у {player.name}, но у того нет наличных!"
        
        steal_money = random.randint(0, player.current_balance // 2 if player.current_balance // 2 > 1 else player.current_balance)
        player.panic = min(100, player.panic + self.power_panic)
        
        if steal_money > 0:
            player.current_balance -= steal_money
        
            return (f"{self.name} украл у {player.name} ${steal_money}.")
        else:
            return f"{self.name} не смог ничего украсть у {player.name}!"
