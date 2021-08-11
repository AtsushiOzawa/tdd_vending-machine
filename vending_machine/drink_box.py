"""飲み物の管理"""


from typing import Any, Dict, List, Optional, Type

from vending_machine.drink import Cola, Drink

_container_type = Dict[Type[Drink], List[Drink]]


class DrinkBox:
    """
    飲み物の管理
    """

    def __init__(self, container: Optional[_container_type] = None):
        """
        コンストラクタ
        """
        # TODO: Keyの型とValueの型が一致する事がわかるようなType Hintに変更する
        # 例としてはKeyがColaでValueがWaterという事が許されてしまう
        if container:
            self.container = container
        else:
            self.container: _container_type = {Cola: [Cola(), Cola(), Cola(), Cola(), Cola()]}

    def __contains__(self, item: Type[Drink]) -> bool:
        """
        指定された飲み物を保持しているかを判定する

        ※0本（空のList）の場合はFalse返す

        Parameters
        ----------
        item : Type[Drink]
            判定対象の飲み物

        Returns
        -------
        bool
            保持しているかどうか
        """
        return (item in self.container) and bool(self.container[item])

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

        ※取り出すものがない場合には例外を投げる（inで確認の上使用する事を想定）

        Parameters
        ----------
        drink : Type[Drink]
            取り出したい飲み物

        Returns
        -------
        Drink
            取り出した飲み物
        """
        result = self.container[drink].pop(0)
        if not self.container[drink]:
            del self.container[drink]
        return result
