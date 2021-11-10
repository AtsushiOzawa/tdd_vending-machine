"""
Main
"""
from typing import Dict, Type

from vending_machine.drink import Cola, Drink, RedBull
from vending_machine.drink_box import DrinkBox
from vending_machine.money import Money
from vending_machine.vending_machine import VendingMachine


def main():
    """
    Buying demonstration.
    """
    drink_price: Dict[Type[Drink], int] = {Cola: 120, RedBull: 200}
    drink_box = DrinkBox(
        {Cola: [Cola(), Cola(), Cola()], RedBull: [RedBull(), RedBull(), RedBull()]}
    )
    vending_machine = VendingMachine(drink_box, drink_price)

    vending_machine.insert(Money.M_100, Money.M_10, Money.M_10)
    cola, change = vending_machine.buy_drink(Cola)
    print(f"Buy: {cola}, Change: {change}")


if __name__ == "__main__":
    main()
