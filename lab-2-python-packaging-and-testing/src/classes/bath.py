from classes.abstract_plumbing import AbstractPlumbing
from classes.form import Form


class Bath(AbstractPlumbing):

    def __init__(self, producer_name, price_in_uah, color, weight_in_kilograms, length_in_centimeters,
                 width_in_centimeters, state, material, form=Form.ASYMMETRIC):
        super().__init__(producer_name, price_in_uah, color,
                         weight_in_kilograms, length_in_centimeters,
                         width_in_centimeters, state, material)
        self.form = form

    def __del__(self):
        return

    def __str__(self):
        return 'Bath(producer_name=' + self.producer_name + ', price_in_uah=' + str(self.price_in_uah) + \
               ', color=' + self.color + ', weight_in_kilograms=' + str(self.weight_in_kilograms) + \
               ', length_in_centimeters=' + str(self.length_in_centimeters) + ', width_in_centimeters=' + \
               str(self.width_in_centimeters) + ', state=' + str(self.state) + ', material=' + str(self.material) + \
               ', form=' + str(self.form) + ')'

    def __repr__(self):
        return 'Bath(producer=' + self.producer_name + ', price=' + str(self.price_in_uah) + \
                ', color=' + self.color + ', weight=' + str(self.weight_in_kilograms) + ', width=' + \
               str(self.width_in_centimeters) + ')'
