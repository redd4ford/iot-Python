from classes.abstract_stove import AbstractStove
from classes.burner_type import BurnerType


class Hob(AbstractStove):

    def __init__(self, producer_name, price_in_uah, color, weight_in_kilograms, length_in_centimeters,
                 width_in_centimeters, state, stove_type, burner_type=BurnerType.INDUCTION, number_of_burners=0):
        super().__init__(producer_name, price_in_uah, color, weight_in_kilograms, length_in_centimeters,
                         width_in_centimeters, state, stove_type)
        self.burner_type = burner_type
        self.number_of_burners = number_of_burners

    def __del__(self):
        return

    def __str__(self):
        return 'Hob(producer_name=' + self.producer_name + ', price_in_uah=' + str(self.price_in_uah) + \
               ', color=' + self.color + ', weight_in_kilograms=' + str(self.weight_in_kilograms) + \
               ', length_in_centimeters=' + str(self.length_in_centimeters) + ', width_in_centimeters=' + \
               str(self.width_in_centimeters) + ', state=' + str(self.state) + ', stove_type=' + \
               str(self.stove_type) + ', burner_type=' + str(self.burner_type) + ', number_of_burners=' + \
               str(self.number_of_burners) + ')'
