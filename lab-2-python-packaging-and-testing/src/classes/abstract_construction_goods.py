from classes.state import State


class AbstractConstructionGoods:

    def __init__(self, producer_name='none', price_in_uah=0, color='black', weight_in_kilograms=0,
                 length_in_centimeters=0, width_in_centimeters=0, state=State.NEW):
        self.producer_name = producer_name
        self.price_in_uah = price_in_uah
        self.color = color
        self.weight_in_kilograms = weight_in_kilograms
        self.length_in_centimeters = length_in_centimeters
        self.width_in_centimeters = width_in_centimeters
        self.state = state

    def __del__(self):
        return

#    def __str__(self):
#       return 'ConstructionGoods(producer_name=' + self.producer_name + ', price_in_uah=' + str(self.price_in_uah) + \
#              ', color=' + self.color + ', weight_in_kilograms=' + str(self.weight_in_kilograms) +\
#              ', length_in_centimeters=' + str(self.length_in_centimeters) + ', width_in_centimeters=' +\
#              str(self.width_in_centimeters) + ', state=' + str(self.state) + ')'
