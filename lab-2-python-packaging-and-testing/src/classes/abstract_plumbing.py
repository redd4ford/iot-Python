from classes.abstract_construction_goods import AbstractConstructionGoods
from classes.material import Material


class AbstractPlumbing(AbstractConstructionGoods):

    def __init__(self, producer_name, price_in_uah, color, weight_in_kilograms, length_in_centimeters,
                 width_in_centimeters, state, material=Material.CAST_IRON):
        super().__init__(producer_name, price_in_uah, color,
                         weight_in_kilograms, length_in_centimeters,
                         width_in_centimeters, state)
        self.material = material

    def __del__(self):
        return

#    def __str__(self):
#       return 'AbstractPlumbing(producer_name=' + self.producer_name + ', price_in_uah=' + str(self.price_in_uah) + \
#              ', color=' + self.color + ', weight_in_kilograms=' + str(self.weight_in_kilograms) + \
#              ', length_in_centimeters=' + str(self.length_in_centimeters) + ', width_in_centimeters=' + \
#               str(self.width_in_centimeters) + ', state=' + str(self.state) + ', material=' + str(self.material) + ')'
