"""飲み物の管理"""


from typing import Any, Dict, List, Optional, Type, TypeVar

from vending_machine.drink import Drink

T = TypeVar("T", bound=Drink)
_container_type = Dict[Type[T], List[T]]


class DrinkBox:
    """
    飲み物の管理
    """

    def __init__(self, container: Optional[Dict[Type[T], List[T]]] = None):
        """
        コンストラクタ
        """
        # TODO: Keyの型とValueの型が一致する事がわかるようなType Hintに変更する
        # 例としてはKeyがColaでValueがWaterという事が許されてしまう
        if container is None:
            self.container: Dict[Type[T], List[T]] = {}
        else:
            self.container = container

    def __contains__(self, item: Type[Drink]) -> bool:
        """
        指定された飲み物を保持しているかを判定する

        ※0本（空のList）の場合はFalse返す

        Parameters
        ----------
        item : Type[T]
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

    T2 = TypeVar("T", bound=Drink)

    def get(self, drink: Type[T2]) -> T2:
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
