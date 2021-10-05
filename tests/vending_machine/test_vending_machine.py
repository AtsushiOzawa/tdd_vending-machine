import pytest

from vending_machine.drink import Cola
from vending_machine.drink_box import DrinkBox
from vending_machine.menu import Menu
from vending_machine.money import Money
from vending_machine.vending_machine import VendingMachine


class TestVendingMachine:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.vending_machine = VendingMachine()

    def test_exists_vending_machine(self):
        assert self.vending_machine

    def test_has_drink_box(self):
        actual = self.vending_machine.drink_box
        assert actual

    def test_initial_inventory(self):
        actual = self.vending_machine.get_inventory()
        expected = []
        assert actual == expected

    def test_revenue(self):
        actual = self.vending_machine.revenue
        expected = 0
        assert actual == expected


class TestMenu:
    def test_not_soldout(self):
        # 在庫はあり販売している
        drink_price = {Cola: 120}
        drink_box = DrinkBox({Cola: [Cola()]})
        vending_machine = VendingMachine(
            drink_box=drink_box, drink_price=drink_price  # type: ignore
        )
        actual = vending_machine.menu
        expected = [Menu(drink=Cola, price=120, soldout=False)]
        assert actual == expected

    def test_soldout(self):
        # 在庫はないけど販売している
        drink_price = {Cola: 120}
        vending_machine = VendingMachine(drink_price=drink_price)  # type: ignore
        actual = vending_machine.menu
        expected = [Menu(drink=Cola, price=120, soldout=True)]
        assert actual == expected

    def test_not_setting_price(self):
        # 在庫はあるけど販売していない（値段が付いていない）
        drink_box = DrinkBox({Cola: [Cola()]})
        vending_machine = VendingMachine(drink_box=drink_box, drink_price={})
        actual = vending_machine.menu
        expected = []
        assert actual == expected


class TestInsert:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.vending_machine = VendingMachine()

    @pytest.mark.parametrize(
        "amount_list, expected_amount", [([], 0), ([10], 10), ([10, 50, 100, 500, 1000], 1660)]
    )
    def test_amount(self, amount_list, expected_amount):
        money_list = [Money(amount) for amount in amount_list]

        self.vending_machine.insert(*money_list)
        assert self.vending_machine.amount == expected_amount

    @pytest.mark.parametrize("money", [Money.M_1, Money.M_2000, Money.M_10000])
    def test_except_money(self, money):
        with pytest.raises(ValueError) as excinfo:
            self.vending_machine.insert(money)

        actual = str(excinfo.value)
        expected = f"Except money error: {money.amount}, [10, 50, 100, 500, 1000] are available."
        assert actual == expected


class TestPayBack:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.vending_machine = VendingMachine()

    @pytest.mark.parametrize("money_list", [[Money.M_10], [Money.M_10, Money.M_1000]])
    def test_money_list(self, money_list):
        self.vending_machine.insert(*money_list)

        actual = self.vending_machine.pay_back()
        expected = money_list
        assert actual == expected

    def test_check_empty(self):
        self.vending_machine.insert(Money.M_10)

        self.vending_machine.pay_back()
        actual = self.vending_machine.money_box
        expected = []
        assert actual == expected


class TestIsBuyDrink:
    def test_is_not_buy_cola_short_money(self):
        drink_box = DrinkBox({Cola: [Cola()]})
        vending_machine = VendingMachine(drink_box=drink_box)
        assert not vending_machine.is_buy_drink(Cola)

    def test_is_not_buy_cola_soldout(self):
        vending_machine = VendingMachine()
        vending_machine.insert(Money.M_100, Money.M_10, Money.M_10)
        assert not vending_machine.is_buy_drink(Cola)

    def test_is_buy_cola(self):
        """
        飲み物が売っている、かつお金が足りている場合、購入可能
        """
        drink_box = DrinkBox({Cola: [Cola()]})
        drink_price = {Cola: 120}
        vending_machine = VendingMachine(
            drink_box=drink_box, drink_price=drink_price  # type: ignore
        )
        vending_machine.insert(Money.M_100, Money.M_10, Money.M_10)
        assert vending_machine.is_buy_drink(Cola)


class TestBuyDrink:
    @pytest.fixture()
    def vending_machine(self):
        drink_box = DrinkBox({Cola: [Cola()]})
        drink_price = {Cola: 120}
        return VendingMachine(drink_box=drink_box, drink_price=drink_price)  # type: ignore

    class TestBuyDrinkCompleted:
        @pytest.fixture(autouse=True)
        def setup(self, vending_machine):
            self.vending_machine = vending_machine
            self.vending_machine.insert(Money.M_100, Money.M_10, Money.M_10)
            self.buy_drink = self.vending_machine.buy_drink(Cola)

        def test_buy_drink(self):
            assert isinstance(self.buy_drink, Cola)

        def test_inventroy(self):
            actual = self.vending_machine.get_inventory()
            expected = []
            assert actual == expected

        def test_revenue(self):
            actual = self.vending_machine.revenue
            expected = 120
            assert actual == expected

    class TestBuyDrinkIncompleted:
        @pytest.fixture(autouse=True)
        def setup(self, vending_machine):
            self.vending_machine = vending_machine

        def test_money_short(self, vending_machine):
            self.vending_machine.insert(Money.M_100, Money.M_10)
            with pytest.raises(ValueError) as excinfo:
                vending_machine.buy_drink(Cola)
            actual = str(excinfo.value)
            expected = "Exception: short of money."
            assert actual == expected
