"""
メニュー
"""
from dataclasses import dataclass
from typing import Type

from vending_machine.drink import Drink


@dataclass(frozen=True)
class Menu:
    """
    メニュー
    """

    drink: Type[Drink]
    price: int
    soldout: bool
