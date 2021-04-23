"""
飲み物
"""
from abc import ABC, abstractmethod


class Drink(ABC):
    """
    飲み物
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        飲み物名

        Returns
        -------
        str
            飲み物名
        """
        pass


class Cola(Drink):
    """
    コーラ
    """

    name = "コーラ"


class Water(Drink):
    """
    水
    """

    name = "水"


class Tea(Drink):
    """
    お茶
    """

    name = "お茶"
