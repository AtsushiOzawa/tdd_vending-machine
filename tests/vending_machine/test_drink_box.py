from vending_machine.drink import Cola, Tea
from vending_machine.drink_box import DrinkBox


class TestInfo:
    def test_exists(self):
        drink_box = DrinkBox(
            {
                Cola: [Cola()],
                Tea: [Tea(), Tea()],
            }
        )
        actual = drink_box.info()
        expected = [
            {
                "drink": Cola,
                "amount": 1,
            },
            {
                "drink": Tea,
                "amount": 2,
            },
        ]
        assert actual == expected

    def test_not_exists(self):
        drink_box = DrinkBox({})
        actual = drink_box.info()
        expected = []
        assert actual == expected


class TestGet:
    def test_normal(self):
        drink_box = DrinkBox({Cola: [Cola(), Cola()]})
        drink = drink_box.get(Cola)

        assert isinstance(drink, Cola)
        assert len(drink_box.container[Cola]) == 1

    def test_delete_key(self):
        drink_box = DrinkBox({Cola: [Cola()]})
        drink_box.get(Cola)

        assert Cola not in drink_box.container


class TestContains:
    def test_exists_drink(self):
        drink_box = DrinkBox({Cola: [Cola()]})
        assert Cola in drink_box

    def test_not_exists_drink(self):
        drink_box = DrinkBox()
        assert Tea not in drink_box

    def test_drink_empty(self):
        drink_box = DrinkBox({Cola: []})
        assert Cola not in drink_box
