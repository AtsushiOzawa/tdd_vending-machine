import pytest

from vending_machine.drink_box import DrinkBox


class TestInfo:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.drink_box = DrinkBox()

    def test_nomal(self):
        actual = self.drink_box.info()
        expected = [
            {
                "name": "cola",
                "amount": 5,
            }
        ]
        assert actual == expected
