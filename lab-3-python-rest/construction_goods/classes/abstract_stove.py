from construction_goods.classes.abstract_construction_goods import AbstractConstructionGoods
from construction_goods.classes.stove_type import StoveType


class AbstractStove(AbstractConstructionGoods):

    def __init__(self, producer_name, price_in_uah, color, weight_in_kilograms, length_in_centimeters,
                 width_in_centimeters, state, stove_type=StoveType.ELECTRIC):
        super().__init__(producer_name, price_in_uah, color, weight_in_kilograms, length_in_centimeters,
                         width_in_centimeters, state)
        self.stove_type = stove_type

    def __del__(self):
        return
