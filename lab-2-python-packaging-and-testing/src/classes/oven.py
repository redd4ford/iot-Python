from classes.abstract_stove import AbstractStove


class Oven(AbstractStove):

    def __init__(self, producer_name, price_in_uah, color, weight_in_kilograms, length_in_centimeters,
                 width_in_centimeters, state, stove_type, volume_in_litres=0, has_backlight=False,
                 has_display=True, number_of_programs=0):
        super().__init__(producer_name, price_in_uah, color, weight_in_kilograms, length_in_centimeters,
                         width_in_centimeters, state, stove_type)
        self.volume_in_litres = volume_in_litres
        self.has_backlight = has_backlight
        self.has_display = has_display
        self.number_of_programs = number_of_programs

    def __del__(self):
        return

    def __str__(self):
        return 'Oven(producer_name=' + self.producer_name + ', price_in_uah=' + str(self.price_in_uah) + \
               ', color=' + self.color + ', weight_in_kilograms=' + str(self.weight_in_kilograms) + \
               ', length_in_centimeters=' + str(self.length_in_centimeters) + ', width_in_centimeters=' + \
               str(self.width_in_centimeters) + ', state=' + str(self.state) + ', stove_type=' + \
               str(self.stove_type) + ', volume_in_litres=' + str(self.volume_in_litres) + ', has_backlight=' + \
               str(self.has_backlight) + ', has_display=' + str(self.has_display) + ', number_of_programs=' + \
               str(self.number_of_programs) + ')'
