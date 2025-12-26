import random
from chip_collection import ChipCollection
from player import Player

class Goose:
    MAX_POWER_PANIC = 20
    MIN_POWER_PANIC = 10
    MAX_STEAL = 5
    STEAL_MONEY_COEF = 4

    def __init__(self, name: str, power_panic: int = 15, steal: int = 2):
        """Инициализация обычного гуся. Сила паники может быть от 10 до 20.  А кража может быть от 1 до 5"""
        self.name = name

        self.power_panic = max(self.MIN_POWER_PANIC, min(power_panic, self.MAX_POWER_PANIC)) # Сила гуся, которая влияет на панику игрока

        self.steal_chips = max(1, min(self.MAX_STEAL, steal))  # Максимальное кол-во фишек, которое гусь может украсть у игрока
    
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
            count_for_steal = 1
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
        
        steal_money = random.randint(0, player.current_balance // self.STEAL_MONEY_COEF if player.current_balance // self.STEAL_MONEY_COEF > 1 else player.current_balance)
        player.panic = min(100, player.panic + self.power_panic)
        
        if steal_money > 0:
            player.current_balance -= steal_money
        
            return (f"{self.name} украл у {player.name} ${steal_money}.")
        else:
            return f"{self.name} не смог ничего украсть у {player.name}!"
        

class HonkGoose(Goose):
    MAX_POWER_PANIC = 40
    MIN_POWER_PANIC = 20
    MAX_STEAL = 5
    MAX_HONK_POWER = 10
    STEAL_MONEY_COEF = 4

    def __init__(self, name: str, honk_power: int = 5, power_panic: int = 25, steal: int = 3):
        """Гусь-крикун с силой крика от 1 до 10. Сила паники может быть от 20 до 40. А кража может быть от 1 до 5."""
        super().__init__(name, power_panic=power_panic, steal=steal)
        
        self.honk_power = max(1, min(self.MAX_HONK_POWER, honk_power))  # Сила крика от 1 до 10, после крика на столько увеличится self.steal_chips
        self.base_steal = self.steal_chips
    
    def __repr__(self) -> str:
        return f"HonkGoose(name={self.name}, honk_power={self.honk_power}, base_steal={self.base_steal})"
    
    def __str__(self) -> str:
        return (f"Гусь-крикун {self.name} (сила крика: {self.honk_power}, "
                f"базовая кража: до {self.steal_chips} фишек)")
    
    def honk(self, player: Player) -> str:
        """
        Гусь кричит на игрока, вызывая панику и увеличивая свою способность к краже.
        """
        if self.steal_chips != self.base_steal:
            return f"Гусь уже кричал!"
        
        print(f"Гусь-крикун {self.name} кричит на игрока {player.name}!!!")
        
        old_panic = player.panic
        player.panic = min(100, player.panic + self.power_panic)
        
        self.steal_chips += self.honk_power
        
        honk_sound = "ГА-" + "А" * self.honk_power + "!"

        self.STEAL_MONEY_COEF = 1 if self.honk_power > 7 else 3
        
        return (f"{self.name} кричит на {player.name}: {honk_sound}\n"
                f"    Паника игрока увеличилась на {player.panic - old_panic} (теперь: {player.panic})\n"
                f"    Способность кражи гуся увеличилась на {self.honk_power} (теперь: до {self.steal_chips} фишек, либо до наличные // {self.STEAL_MONEY_COEF} наличных)")
    
    def enlarget_steal_chip(self, player: Player) -> str:
        """
        Усиленная кража фишек после крика - использует увеличенную способность кражи.
        """
        current_steal = self.steal_chips - self.honk_power

        if current_steal != self.base_steal:
            print(f"Гусь не кричал или буст уже использован! Будет использована обычная кража...")
            self.steal_chips = self.base_steal
        else:
            print(f"Гусь-крикун {self.name} использует усиленную кражу после крика!")
        
        result = self.steal_chip(player)

        self.steal_chips = self.base_steal
        
        return result
    
    def enlarget_steal_money(self, player: Player) -> str:
        """
        Усиленная кража денег после крика - использует увеличенную способность кражи.
        """
        print(f"Гусь-крикун {self.name} использует усиленную кражу после крика!")
        
        result = self.steal_money(player)
        
        self.steal_chips -= self.honk_power
        self.STEAL_MONEY_COEF = 4
        
        return result
