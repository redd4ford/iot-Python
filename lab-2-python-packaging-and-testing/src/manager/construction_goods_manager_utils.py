from classes.state import State
from classes.material import Material
from classes.form import Form
from classes.bath import Bath
from classes.sink import Sink
from classes.toilet import Toilet
import doctest


class ConstructionGoodsManagerUtils:
    def __init__(self):
        pass

    @staticmethod
    def sort_by_weight(list_of_goods, reverse=False):
        """
        returns a list of objects sorted in ascending by weight_in_kilograms (4th field)
        >>> bath = Bath('Ukraine', 900, 'white', 500, 200, 90, State.NEW, Material.STEEL, Form.OVAL)
        >>> sink = Sink('China', 1200, 'black', 150, 60, 60, 20, State.NEW, Material.STEEL, Form.OVAL)
        >>> toilet = Toilet('USA', 700, 'blue', 200, 20, 20, State.NEW, Material.STEEL, Form.OVAL)
        >>> print(str(ConstructionGoodsManagerUtils.sort_by_weight([bath, sink, toilet]))) #doctest: +ELLIPSIS
        [Sink(...weight=150...), Toilet(...weight=200...), Bath(...weight=500...)]
        """
        return sorted(list_of_goods, key=lambda good: good.weight_in_kilograms, reverse=reverse)

    @staticmethod
    def sort_by_width(list_of_goods, reverse=False):
        """
        returns a list of objects sorted in ascending by width_in_centimeters (6th field)
        >>> bath = Bath('Ukraine', 900, 'white', 500, 200, 90, State.NEW, Material.STEEL, Form.OVAL)
        >>> sink = Sink('China', 1200, 'black', 150, 60, 60, 20, State.NEW, Material.STEEL, Form.OVAL)
        >>> toilet = Toilet('USA', 700, 'blue', 200, 20, 20, State.NEW, Material.STEEL, Form.OVAL)
        >>> print(str(ConstructionGoodsManagerUtils.sort_by_width([bath, sink, toilet]))) #doctest: +ELLIPSIS
        [Toilet(...width=20), Sink(...width=60), Bath(...width=90)]
        """
        return sorted(list_of_goods, key=lambda good: good.width_in_centimeters, reverse=reverse)

    @staticmethod
    def sort_by_producer_name(list_of_goods, reverse=True):
        """
        returns a list of objects sorted in descending by producer_name (1st field)
        >>> bath = Bath('Ukraine', 900, 'white', 500, 200, 90, State.NEW, Material.STEEL, Form.OVAL)
        >>> sink = Sink('China', 1200, 'black', 150, 60, 60, 20, State.NEW, Material.STEEL, Form.OVAL)
        >>> toilet = Toilet('USA', 700, 'blue', 200, 20, 20, State.NEW, Material.STEEL, Form.OVAL)
        >>> print(str(ConstructionGoodsManagerUtils.sort_by_producer_name([bath, sink, toilet]))) #doctest: +ELLIPSIS
        [Bath(producer=Ukraine...), Toilet(producer=USA...), Sink(producer=China...)]
        """
        return sorted(list_of_goods, key=lambda good: good.producer_name, reverse=reverse)

    @staticmethod
    def sort_by_color(list_of_goods, reverse=True):
        """
        returns a list of objects sorted in descending by color (3rd field)
        >>> bath = Bath('Ukraine', 900, 'white', 500, 200, 90, State.NEW, Material.STEEL, Form.OVAL)
        >>> sink = Sink('China', 1200, 'black', 150, 60, 60, 20, State.NEW, Material.STEEL, Form.OVAL)
        >>> toilet = Toilet('USA', 700, 'blue', 200, 20, 20, State.NEW, Material.STEEL, Form.OVAL)
        >>> print(str(ConstructionGoodsManagerUtils.sort_by_color([bath, sink, toilet]))) #doctest: +ELLIPSIS
        [Bath(...color=white...), Toilet(...color=blue...), Sink(...color=black...)]
        """
        return sorted(list_of_goods, key=lambda good: good.color, reverse=reverse)


if __name__ == '__main__':
    doctest.testmod(verbose=True)
