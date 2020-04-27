class Hotel:
    max_number_of_beds_in_room: int = 3

    def __init__(self, name=None, visitors_per_year=0, number_of_rooms=0, rating_on_booking=0.0,
                 type_of_hotel='hotel', city='Lviv'):
        self.name = name
        self.visitors_per_year = visitors_per_year
        self.number_of_rooms = number_of_rooms
        self.rating_on_booking = rating_on_booking
        self.type_of_hotel = type_of_hotel
        self.city = city

    def __del__(self):
        print('deleted ' + self.__class__.__name__)
        return

    def __str__(self):
        return 'Hotel(name=' + self.name + ', visitors_per_year=' + str(self.visitors_per_year) + \
               ', number_of_rooms=' + str(self.number_of_rooms) + \
               ', rating_on_booking=' + str(self.rating_on_booking) + \
               ', type_of_hotel=' + self.type_of_hotel + ', city=' + self.city + ')'

    @staticmethod
    def get_max_number_of_beds_in_room():
        return Hotel.max_number_of_beds_in_room

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_visitors_per_year(self):
        return self.visitors_per_year

    def set_visitors_per_year(self, visitors_per_year):
        self.visitors_per_year = visitors_per_year

    def get_number_of_rooms(self):
        return self.number_of_rooms

    def set_number_of_rooms(self, number_of_rooms):
        self.number_of_rooms = number_of_rooms

    def get_rating_on_booking(self):
        return self.rating_on_booking

    def set_rating_on_booking(self, rating_on_booking):
        self.rating_on_booking = rating_on_booking

    def get_type_of_hotel(self):
        return self.type_of_hotel

    def set_type_of_hotel(self, type_of_hotel):
        self.type_of_hotel = type_of_hotel

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city
