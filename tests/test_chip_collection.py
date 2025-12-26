from src.chip_collection import ChipCollection


def test_initialization() -> None:
    """Проверяет корректность инициализации объекта"""
    cc1 = ChipCollection()
    assert cc1.chips == [0, 0, 0, 0]
    
    cc2 = ChipCollection(1, 2, 3, 4)
    assert cc2.chips == [1, 2, 3, 4]


def test_repr() -> None:
    """Проверяет работу магического метода __repr__"""
    cc = ChipCollection(1, 2, 3, 4)
    assert repr(cc) == "ChipCollection(chip_1=1, chip_5=2, chip_25=3, chip_100=4)"


def test_str() -> None:
    """Проверяет работу магического метода __str__"""
    cc = ChipCollection(1, 2, 3, 4)
    assert "1×1$, 2×5$, 3×25$, 4×100$" in str(cc)


def test_iter() -> None:
    """Проверяет корректность итерации по объекту"""
    cc = ChipCollection(1, 2, 3, 4)
    result = list(cc)
    assert result == [(1, 1), (2, 5), (3, 25), (4, 100)]


def test_setitem() -> None:
    """Проверяет установку значений по индексу"""
    cc = ChipCollection()
    cc[0] = 10
    cc[1] = 20
    cc[2] = 30
    cc[3] = 40
    assert cc.chips == [10, 20, 30, 40]


def test_getitem() -> None:
    """Проверяет получение значений по индексу и срезы"""
    cc = ChipCollection(1, 2, 3, 4)
    assert cc[0] == 1
    assert cc[1] == 2
    assert cc[2] == 3
    assert cc[3] == 4
    assert cc[0:2] == [1, 2]


def test_len() -> None:
    """Проверяет работу магического метода __len__"""
    cc = ChipCollection()
    assert len(cc) == 4


def test_iadd() -> None:
    """Проверяет операцию сложения с присваиванием (+=)"""
    cc1 = ChipCollection(1, 2, 3, 4)
    cc2 = ChipCollection(4, 3, 2, 1)
    cc1 += cc2
    assert cc1.chips == [5, 5, 5, 5]


def test_imul() -> None:
    """Проверяет операцию умножения с присваиванием (*=)"""
    cc = ChipCollection(1, 2, 3, 4)
    cc *= 3
    assert cc.chips == [3, 6, 9, 12]


def test_isub() -> None:
    """Проверяет операцию вычитания с присваиванием (-=)"""
    cc1 = ChipCollection(10, 10, 10, 10)
    cc2 = ChipCollection(1, 2, 3, 4)
    cc1 -= cc2
    assert cc1.chips == [9, 8, 7, 6]


def test_ge() -> None:
    """Проверяет операцию сравнения больше или равно (>=)"""
    cc1 = ChipCollection(5, 5, 5, 5)
    cc2 = ChipCollection(3, 3, 3, 3)
    assert cc1 >= cc2
    assert not cc2 >= cc1


def test_no_zero_chips() -> None:
    """Проверяет метод получения индексов ненулевых фишек"""
    cc1 = ChipCollection(0, 2, 0, 4)
    assert cc1.no_zero_chips() == [1, 3]
    
    cc2 = ChipCollection(1, 0, 3, 0)
    assert cc2.no_zero_chips() == [0, 2]