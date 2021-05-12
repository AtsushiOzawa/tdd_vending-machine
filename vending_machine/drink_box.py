"""飲み物の管理"""


from typing import Any, Dict, List, Type

from vending_machine.drink import Cola, Drink


class DrinkBox:
    """
    飲み物の管理
    """

    def __init__(self):
        """
        コンストラクタ
        """
        # TODO: Keyの型とValueの型が一致する事がわかるようなType Hintに変更する
        # 例としてはKeyがColaでValueがWaterという事が許されてしまう
        self.container: Dict[Type[Drink], List[Drink]] = {
            Cola: [Cola(), Cola(), Cola(), Cola(), Cola()]
        }

    def info(self) -> List[Dict[str, Any]]:
        """
        管理している飲み物の情報を返す。

        Returns
        -------
        List[Dict[str, Any]]
            管理している飲み物の情報
        """
        return [
            {"name": drink.name, "amount": len(drink_list)}
            for drink, drink_list in self.container.items()
        ]
