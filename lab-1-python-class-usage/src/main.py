from src import Hotel


def main():
    first_hotel = Hotel('Hotel#1')
    second_hotel = Hotel('Hotel#2', 12000, 500, 8.6, 'resort')
    third_hotel = Hotel('Hotel#3', 5600, 90, 9.9, 'hostel', 'Kyiv')
    hotels = [first_hotel, second_hotel, third_hotel]
    [(print(element), print(element.__repr__()), print('\n')) for element in hotels]
    print('calling static method: ')
    print(Hotel.get_max_number_of_beds_in_room())


if __name__ == '__main__':
    main()
