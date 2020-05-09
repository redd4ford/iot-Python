from construction_goods.classes.state import State
from construction_goods.classes.material import Material
from construction_goods.classes.form import Form
from construction_goods.classes.bath import Bath
from construction_goods.classes.sink import Sink
from construction_goods.classes.toilet import Toilet
import doctest


class ConstructionGoodsManager:
    def __init__(self, list_of_goods=None):
        if list_of_goods is None:
            list_of_goods = []
        self.list_of_goods = list_of_goods

    def find_cheaper_than(self, price_in_uah: int):
        """
        returns list of objects that have obj.price_in_uah < price_in_uah: int)
        >>> bath = Bath('Ukraine', 900, 'white', 500, 200, 90, State.NEW, Material.STEEL, Form.OVAL)
        >>> sink = Sink('China', 1200, 'black', 150, 60, 60, 20, State.NEW, Material.STEEL, Form.OVAL)
        >>> toilet = Toilet('USA', 700, 'blue', 200, 20, 20, State.NEW, Material.STEEL, Form.OVAL)
        >>> print(str(ConstructionGoodsManager([bath, sink, toilet]).find_cheaper_than(1000))) #doctest: +ELLIPSIS
        [Bath(...price=900...), Toilet(...price=700...)]
        """
        return list(filter(lambda good: good.price_in_uah < price_in_uah, self.list_of_goods))


if __name__ == '__main__':
    doctest.testmod(verbose=True)
