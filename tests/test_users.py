from src.users import UsersCazino
from src.player import Player


def test_initialization() -> None:
    """Проверяет корректность инициализации объекта"""
    uc = UsersCazino()
    assert uc.users == {}


def test_repr() -> None:
    """Проверяет работу магического метода __repr__"""
    uc = UsersCazino()
    p1 = Player("Dustin")
    p2 = Player("player")
    uc.users = {"user1": p1, "user2": p2}
    assert "UsersCazino" in repr(uc)
    assert "users" in repr(uc)


def test_iter() -> None:
    """Проверяет корректность итерации по ключам объекта"""
    uc = UsersCazino()
    uc.users = {"user1": Player("Dustin"), "user2":  Player("player")}
    keys = list(iter(uc))
    assert keys == ["user1", "user2"]


def test_getitem() -> None:
    """Проверяет получение значений по ключу"""
    uc = UsersCazino()
    uc.users = {"user1": Player("Dustin"), "user2":  Player("player")}
    assert uc["user1"].name == "Dustin"
    assert uc["user2"].name == "player"


def test_setitem() -> None:
    """Проверяет установку значений по ключу"""
    uc = UsersCazino()
    p1 = Player("Dustin")
    p2 = Player("player")
    uc["user1"] = p1
    uc["user2"] = p2
    assert uc.users == {"user1": p1, "user2": p2}


def test_delitem() -> None:
    """Проверяет удаление элементов по ключу"""
    uc = UsersCazino()
    p1 = Player("Dustin")
    p2 = Player("player")
    uc.users = {"user1": p1, "user2": p2}
    del uc["user1"]
    assert "user1" not in uc.users
    assert uc.users == {"user2": p2}


def test_contains() -> None:
    """Проверяет операцию проверки наличия ключа"""
    uc = UsersCazino()
    uc.users = {"user1": Player("Dustin")}
    assert "user1" in uc
    assert "user2" not in uc


def test_len() -> None:
    """Проверяет работу магического метода __len__"""
    uc = UsersCazino()
    p1 = Player("Dustin")
    p2 = Player("player")
    uc.users = {"user1": p1, "user2": p2}
    assert len(uc) == 2


def test_add() -> None:
    """Проверяет операцию сложения двух коллекций"""
    p1 = Player("Dustin")
    p2 = Player("player")

    uc1 = UsersCazino()
    uc1.users = {"user1": p1}
    
    uc2 = UsersCazino()
    uc2.users = {"user2": p2}
    
    result = uc1 + uc2
    assert result.users == {"user1": p1, "user2": p2}


def test_keys() -> None:
    """Проверяет метод получения ключей"""
    uc = UsersCazino()
    p1 = Player("Dustin")
    p2 = Player("player")
    uc.users = {"user1": p1, "user2": p2}
    assert list(uc.keys()) == ["user1", "user2"]


def test_values() -> None:
    """Проверяет метод получения значений"""
    uc = UsersCazino()
    p1 = Player("Dustin")
    p2 = Player("player")
    uc.users = {"user1": p1, "user2": p2}
    assert list(uc.values()) == [p1, p2]


def test_items() -> None:
    """Проверяет метод получения пар ключ-значение"""
    uc = UsersCazino()
    p1 = Player("Dustin")
    p2 = Player("player")
    uc.users = {"user1": p1, "user2": p2}
    assert list(uc.items()) == [("user1", p1), ("user2", p2)]