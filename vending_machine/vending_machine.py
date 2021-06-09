"""
飲み物の自動販売機
"""

from typing import Any, Dict, List, Type

from vending_machine.drink import Cola, Drink
from vending_machine.drink_box import DrinkBox
from vending_machine.menu import Menu
from vending_machine.money import Money


class VendingMachine:
    """
    飲み物の自動販売機
    """

    def __init__(self):
        """
        初期処理
        """
        self.money_box = []
        self.allow_money = (
            Money.M_10,
            Money.M_50,
            Money.M_100,
            Money.M_500,
            Money.M_1000,
        )
        self.drink_box = DrinkBox()
        self.drink_price = {Cola: 120}

    @property
    def total(self) -> int:
        """
        投入金額を返す

        Returns
        -------
        int
            投入金額
        """
        return sum(money.amount for money in self.money_box)

    @property
    def menu(self) -> List[Menu]:
        """
        自販機のメニューを返す

        Returns
        -------
        List[Menu]
            自販機のメニュー
        """

        def f(drink: Type[Drink], price: int) -> Menu:
            return Menu(drink=drink, price=price, soldout=not bool(self.drink_box.container[drink]))

        result = [f(drink, price) for drink, price in self.drink_price.items()]
        return result

    def insert(self, *money_list: Money) -> None:
        """
        お金を投入。

        Parameters
        ----------
        money_list : Money
            投入金額
        """
        for money in money_list:
            if money not in self.allow_money:
                allow_amount = [m.amount for m in self.allow_money]
                raise ValueError(
                    f"Except money error: {money.amount}, {allow_amount} are available."
                )
        self.money_box += [*money_list]

    def pay_back(self) -> List[Money]:
        """
        投入金額の総計を釣り銭として出力

        Returns
        -------
        Money
            投入金額の総計
        """
        money_paid_back = self.money_box
        self.money_box = []
        return money_paid_back

    def get_inventory(self) -> List[Dict[str, Any]]:
        """
        在庫を返す

        Returns
        -------
        List[Dict[str, Any]]
            在庫
        """
        return self.drink_box.info()
