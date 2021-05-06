"""飲み物の管理"""


from typing import Any, Dict, List

from vending_machine.drink import Cola


class DrinkBox:
    """
    飲み物の管理
    """

    def __init__(self):
        """
        コンストラクタ
        """
        self.container = {
            Cola: {
                "value": [Cola(), Cola(), Cola(), Cola(), Cola()],
                "price": 120,
            }
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
            {"name": drink.name, "amount": len(info["value"]), "price": info["price"]}
            for drink, info in self.container.items()
        ]

    # TODO: drinkクラスのnameを日本語に変更 driver ozawa
    # TODO: priceを自販機側に移動
    # 宿題: 今のブランチをforkして、yamap55 をcollaborator に追加、yamap55にリポジトリを連絡 by ozawa
