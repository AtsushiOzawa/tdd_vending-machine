import pytest

from vending_machine.drink import Cola
from vending_machine.drink_box import DrinkBox


class TestInfo:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.drink_box = DrinkBox()

    def test_normal(self):
        actual = self.drink_box.info()
        expected = [
            {
                "drink": Cola,
                "amount": 5,
            }
        ]
        assert actual == expected

    def test_get(self):
        assert len(self.drink_box.container[Cola]) == 5

        drink = self.drink_box.get(Cola)

        assert isinstance(drink, Cola)
        assert len(self.drink_box.container[Cola]) == 4
