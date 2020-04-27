from classes.abstract_plumbing import AbstractPlumbing
from classes.form import Form


class Sink(AbstractPlumbing):

    def __init__(self, producer_name, price_in_uah, color, weight_in_kilograms, length_in_centimeters,
                 width_in_centimeters, state, material, depth_in_centimeters=0,
                 height_in_centimeters=0, has_mixer_hole=False, form=Form.ASYMMETRIC):
        super().__init__(producer_name, price_in_uah, color,
                         weight_in_kilograms, length_in_centimeters,
                         width_in_centimeters, state, material)
        self.depth_in_centimeters = depth_in_centimeters
        self.height_in_centimeters = height_in_centimeters
        self.has_mixer_hole = has_mixer_hole
        self.form = form

    def __del__(self):
        return

    def __str__(self):
        return 'Sink(producer_name=' + self.producer_name + ', price_in_uah=' + str(self.price_in_uah) + \
               ', color=' + self.color + ', weight_in_kilograms=' + str(self.weight_in_kilograms) + \
               ', length_in_centimeters=' + str(self.length_in_centimeters) + ', width_in_centimeters=' + \
               str(self.width_in_centimeters) + ', state=' + str(self.state) + ', material=' + str(self.material) + \
               ', depth_in_centimeters=' + str(self.depth_in_centimeters) + ', height_in_centimeters=' + \
               str(self.height_in_centimeters) + ', has_mixer_hole=' + str(self.has_mixer_hole) + ', form=' + \
               str(self.form) + ')'

    def __repr__(self):
        return 'Sink(producer=' + self.producer_name + ', price=' + str(self.price_in_uah) + \
                ', color=' + self.color + ', weight=' + str(self.weight_in_kilograms) + ', width=' + \
               str(self.width_in_centimeters) + ')'
