from classes.abstract_plumbing import AbstractPlumbing
from classes.drain_type import DrainType


class Toilet(AbstractPlumbing):

    def __init__(self, producer_name, price_in_uah, color, weight_in_kilograms, length_in_centimeters,
                 width_in_centimeters, state, material, has_tank=False, has_sit=False,
                 drain_type=DrainType.VERTICAL):
        super().__init__(producer_name, price_in_uah, color,
                         weight_in_kilograms, length_in_centimeters,
                         width_in_centimeters, state, material)
        self.has_tank = has_tank
        self.has_sit = has_sit
        self.drain_type = drain_type

    def __del__(self):
        return

    def __str__(self):
        return 'Toilet(producer_name=' + self.producer_name + ', price_in_uah=' + str(self.price_in_uah) + \
               ', color=' + self.color + ', weight_in_kilograms=' + str(self.weight_in_kilograms) + \
               ', length_in_centimeters=' + str(self.length_in_centimeters) + ', width_in_centimeters=' + \
                str(self.width_in_centimeters) + ', state=' + str(self.state) + ', material=' + str(self.material) + \
               ', has_tank=' + str(self.has_tank) + ', has_sit=' + str(self.has_sit) + ', drain_type=' + \
               str(self.drain_type) + ')'

    def __repr__(self):
        return 'Toilet(producer=' + self.producer_name + ', price=' + str(self.price_in_uah) + \
                ', color=' + self.color + ', weight=' + str(self.weight_in_kilograms) + ', width=' + \
               str(self.width_in_centimeters) + ')'
