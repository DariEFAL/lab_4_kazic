from unittest.mock import patch
from typing import Dict, Any

from src.player import Player


def test_player_initialization() -> None:
    """Проверяет корректность инициализации игрока"""
    player = Player("Иван", 100)
    assert player.name == "Иван"
    assert player.current_balance == 100
    assert player.chips.chips == [0, 0, 0, 0]
    assert player.panic == 0


def test_player_repr() -> None:
    """Проверяет работу магического метода __repr__"""
    player = Player("Иван", 100)
    assert "Player" in repr(player)
    assert "Иван" in repr(player)
    assert "100" in repr(player)


def test_player_str() -> None:
    """Проверяет работу магического метода __str__"""
    player = Player("Иван", 100)
    result = str(player)
    assert "Игрок: Иван" in result
    assert "Баланс: $100" in result
    assert "Уровень паники: 0 из 100" in result


def test_buy_chips_success() -> None:
    """Проверяет успешную покупку фишек"""
    player = Player("Иван", 100)
    result = player.buy_chips(5, 2, 1, 0)
    
    assert player.current_balance == 60
    assert player.chips.chips == [5, 2, 1, 0]
    assert "купил фишки" in result

test_buy_chips_insufficient_balance
def () -> None:
    """Проверяет попытку покупки фишек при недостаточном балансе"""
    player = Player("Иван", 10)
    result = player.buy_chips(0, 0, 1, 0)
    
    assert player.current_balance == 10
    assert player.chips.chips == [0, 0, 0, 0]
    assert "имеет недостаточно денег" in result


def test_rulette_zero_bet() -> None:
    """Проверяет попытку поставить 0 фишек в рулетке"""
    player = Player("Иван", 100)
    player.buy_chips(10, 2, 1, 0)
    result = player.rulette()
    
    assert "нельзя поставить 0 фишек" in result


def test_rulette_insufficient_chips() -> None:
    """Проверяет попытку поставить больше фишек, чем есть"""
    player = Player("Иван", 100)
    player.buy_chips(5, 0, 0, 0)
    result = player.rulette(10, 0, 0, 0)
    
    assert "нельзя поставить несуществующие фишки" in result


@patch('random.choice')
def test_rulette_win(mock_random) -> None:
    """Проверяет выигрыш в рулетке"""
    mock_random.return_value = 3
    
    player = Player("Иван", 100)
    player.buy_chips(10, 2, 0, 0)
    result = player.rulette(5, 1, 0, 0)
    
    assert player.chips.chips == [20, 4, 0, 0]
    assert "Победа" in result


@patch('random.choice')
def test_rulette_loss(mock_random) -> None:
    """Проверяет проигрыш в рулетке"""
    mock_random.return_value = 0 
    
    player = Player("Иван", 100)
    player.buy_chips(10, 2, 0, 0)
    result = player.rulette(5, 1, 0, 0)
    
    assert player.chips.chips == [5, 1, 0, 0]
    assert "Проигрыш" in result


def test_transfer_money_success() -> None:
    """Проверяет успешный перевод фишек в деньги"""
    player = Player("Иван", 100)
    player.buy_chips(10, 2, 1, 0)
    
    initial_balance = player.current_balance
    result = player.transfer_money(5, 1, 1, 0)
    
    assert player.current_balance == initial_balance + (5*1 + 1*5 + 1*25)
    assert player.chips.chips == [5, 1, 0, 0]
    assert "перевел фишки" in result


def test_transfer_money_insufficient_chips() -> None:
    """Проверяет попытку перевода фишек при их недостатке"""
    player = Player("Иван", 100)
    player.buy_chips(5, 0, 0, 0)
    
    initial_balance = player.current_balance
    result = player.transfer_money(10, 0, 0, 0)
    
    assert player.current_balance == initial_balance
    assert player.chips.chips == [5, 0, 0, 0]
    assert "имеет недостаточно фишек" in result