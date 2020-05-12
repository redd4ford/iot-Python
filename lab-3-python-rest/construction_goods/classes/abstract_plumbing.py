from construction_goods.classes.abstract_construction_goods import AbstractConstructionGoods
from construction_goods.classes.material import Material


class AbstractPlumbing(AbstractConstructionGoods):

    def __init__(self, producer_name, price_in_uah, color, weight_in_kilograms, length_in_centimeters,
                 width_in_centimeters, state, material=Material.CAST_IRON):
        super().__init__(producer_name, price_in_uah, color,
                         weight_in_kilograms, length_in_centimeters,
                         width_in_centimeters, state)
        self.material = material

    def __del__(self):
        return
