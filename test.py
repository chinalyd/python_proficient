from duo1 import ChadianCar, Car
my_tesla = ChadianCar('Benz', 'E350L', 2017)
print(my_tesla.get_car_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_beetle = Car('Volkswagen', 'Beetles', 1956)
print(my_beetle.get_car_name())
