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
            return (f"{self.name} украл у {player.name}: {stolen[0]}x1$, {stolen[1]}x5$, "
                    f"{stolen[2]}x25$, {stolen[3]}x100$. \n"
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
        current_steal = self.steal_chips - self.honk_power

        if current_steal != self.base_steal:
            print(f"Гусь не кричал или буст уже использован! Будет использована обычная кража...")
            self.steal_chips = self.base_steal
        else:
            print(f"Гусь-крикун {self.name} использует усиленную кражу после крика!")
        
        result = self.steal_money(player)
        
        self.steal_chips = self.base_steal
        self.STEAL_MONEY_COEF = 4
        
        return result


class PlayGoose(Goose, Player):
    def __init__(self, name: str):
        """Гусь-игрок просто кайфует от жизни. Может украсть только фишки. Может покрутить рулетку."""
        Goose.__init__(self, name, power_panic=10, steal=3)
        Player.__init__(self, name, balance=0)
    
    def __repr__(self) -> str:
        return f"PlayGoose(name={self.name}, power_panic={self.power_panic}, steal={self.steal_chips}), chips={self.chips}"
    
    def __str__(self) -> str:
        return (f"Гусь-игрок {self.name}\n"
                f"Кража до {self.steal_chips}\n"
                f"{self.chips}")
    
    def steal_money(self, player: Player = None) -> str:
        return f"Гусь-игрок не интересуется обычными деньгами. Ему нужны фишки!"
    
    def buy_chips(self, *arg, **kwarqs) -> str:
        return f"Гусь-игрок не покупает фишки. Он их ворует..."
    
    def transfer_money(self, *arg, **kwargs) -> str:
        return f"Гусь-игрок не нуждается в деньгах! Только фишки..."
    
    def steal_chip(self, player) -> str:
        """Гусь пытается украсть фишки у игрока."""
        print(f"Гусь-игрок, {self.name}, бежит на игрока {player.name}!!!")

        if not player.chips.no_zero_chips():
            player.panic = min(100, player.panic + self.power_panic // 2)
            return f"{self.name} пытается украсть у {player.name}, но у того нет фишек!"
        
        random_steal_chips = random.randint(1, self.steal_chips)
        
        stolen = ChipCollection()
        
        while random_steal_chips != 0 and player.chips.no_zero_chips():
            index = random.choice(player.chips.no_zero_chips())
            count_for_steal = 1
            stolen[index] += count_for_steal 

            player.chips[index] -= count_for_steal 
            random_steal_chips -= 1

        player.panic = min(100, player.panic + self.power_panic)
        
        if sum(i[0] for i in stolen) > 0:
            self.chips += stolen
            
            return (f"{self.name} украл у {player.name}: {stolen[0]}x1$, {stolen[1]}x5$, "
                    f"{stolen[2]}x25$, {stolen[3]}x100$.")
        else:
            return f"{self.name} не смог ничего украсть у {player.name}!"
        
    

import random
from chip_collection import ChipCollection
from player import Player

def test_playgoose_init():
    """Тест 1: Проверка инициализации PlayGoose"""
    print("=" * 50)
    print("Тест 1: Инициализация PlayGoose")
    print("=" * 50)
    
    goose = PlayGoose("ГусьИгрок")
    
    print(f"Создан: {goose}")
    print(f"repr: {repr(goose)}")
    
    # Проверяем базовые атрибуты
    assert goose.name == "ГусьИгрок", "Имя должно быть 'ГусьИгрок'"
    assert goose.power_panic == 10, "Сила паники должна быть 10"
    assert goose.steal_chips == 3, "Кража должна быть до 3 фишек"
    assert goose.current_balance == 0, "Баланс должен быть 0"
    
    print("✅ Тест 1 пройден: PlayGoose инициализируется корректно\n")

def test_playgoose_no_money_operations():
    """Тест 2: Проверка, что гусь-игрок не работает с обычными деньгами"""
    print("=" * 50)
    print("Тест 2: PlayGoose отвергает денежные операции")
    print("=" * 50)
    
    goose = PlayGoose("ГусьБандит")
    player = Player("Вася", balance=100)
    
    # Тестируем запрещенные методы
    result1 = goose.steal_money()
    print(f"steal_money(): {result1}")
    assert "не интерисуется обычными деньгами" in result1
    
    result2 = goose.buy_chips()
    print(f"buy_chips(): {result2}")
    assert "не покупает фишки" in result2
    
    result3 = goose.transfer_money()
    print(f"transfer_money(): {result3}")
    assert "не нуждается в деньгах" in result3
    
    print("✅ Тест 2 пройден: PlayGoose корректно отвергает денежные операции\n")

def test_playgoose_steal_chips_empty():
    """Тест 3: Попытка кражи фишек у игрока без фишек"""
    print("=" * 50)
    print("Тест 3: Кража фишек у бедного игрока")
    print("=" * 50)
    
    goose = PlayGoose("Воришка")
    player = Player("Бедняга", balance=0)
    
    # У игрока нет фишек изначально
    result = goose.steal_chip(player)
    print(f"Результат кражи: {result}")
    
    assert "но у того нет фишек" in result
    assert player.panic > 0, "Паника должна увеличиться"
    
    print(f"Паника игрока после неудачной кражи: {player.panic}")
    print("✅ Тест 3 пройден: PlayGoose корректно обрабатывает отсутствие фишек\n")

def test_playgoose_steal_chips_success():
    """Тест 4: Успешная кража фишек"""
    print("=" * 50)
    print("Тест 4: Успешная кража фишек")
    print("=" * 50)
    
    # Фиксируем случайность для теста
    random.seed(42)
    
    goose = PlayGoose("Профи")
    player = Player("Богач", balance=200)
    
    # Даем игроку фишки
    player.buy_chips(chip_1=5, chip_5=3, chip_25=2)
    print(f"У игрока до кражи: {player.chips}")
    print(f"У гуся до кражи: {goose.chips}")
    
    # Пытаемся украсть
    result = goose.steal_chip(player)
    print(f"\nРезультат кражи: {result}")
    
    # Проверяем результаты
    print(f"\nУ игрока после кражи: {player.chips}")
    print(f"У гуся после кражи: {goose.chips}")
    print(f"Паника игрока: {player.panic}")
    
    # Проверяем, что что-то изменилось
    total_stolen = sum(goose.chips.chips)
    assert total_stolen > 0, "Гусь должен был что-то украсть"
    assert player.panic > 0, "Паника игрока должна увеличиться"
    
    print("✅ Тест 4 пройден: PlayGoose успешно крадет фишки\n")

def run_all_tests():
    """Запуск всех тестов"""
    print("🧪 ЗАПУСК ТЕСТОВ ДЛЯ PlayGoose 🧪")
    print("=" * 60)
    
    try:
        test_playgoose_init()
        test_playgoose_no_money_operations()
        test_playgoose_steal_chips_empty()
        test_playgoose_steal_chips_success()
        
        print("=" * 60)
        print("🎉 ВСЕ 4 ТЕСТА УСПЕШНО ПРОЙДЕНЫ! 🎉")
        print("=" * 60)
        
    except AssertionError as e:
        print(f"\n❌ ОШИБКА В ТЕСТЕ: {e}")
        print("=" * 60)
    except Exception as e:
        print(f"\n⚠️ НЕОЖИДАННАЯ ОШИБКА: {e}")
        print("=" * 60)

# Запуск тестов
if __name__ == "__main__":
    run_all_tests()