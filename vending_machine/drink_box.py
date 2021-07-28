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
            {"drink": drink, "amount": len(drink_list)}
            for drink, drink_list in self.container.items()
        ]

    def get(self, drink: Type[Drink]) -> Drink:
        # TODO: 入出力の型が一致するようにType Hintを設定する
        """
        飲み物を取り出す。

        Parameters
        ----------
        drink : Type[Drink]
            取り出したい飲み物

        Returns
        -------
        Drink
            取り出した飲み物
        """
        # TODO: 飲み物がKeyとして存在しない場合の処理を追加
        # TODO: 飲み物の本数が0の場合の処理を追加
        return self.container[drink].pop(0)
