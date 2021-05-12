import pytest

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
        expected = [
            {
                "name": "cola",
                "amount": 5,
            }
        ]

        assert actual == expected


class TestInsert:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.vending_machine = VendingMachine()

    @pytest.mark.parametrize(
        "amount_list, expected_total", [([], 0), ([10], 10), ([10, 50, 100, 500, 1000], 1660)]
    )
    def test_total(self, amount_list, expected_total):
        money_list = [Money(amount) for amount in amount_list]

        self.vending_machine.insert(*money_list)
        assert self.vending_machine.total == expected_total

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
