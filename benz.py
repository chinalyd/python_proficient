class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' '+self.manufacturer + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This is a new car, and the current reading meter range is " + str(self.odometer_reading) + " KM.")
class Bmw(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery_size = "6 cylinder engine"
    def motor(self):
        print("This BMW's motor is ",str(self.battery_size))
my_tesla = Bmw('precious horse', '535Li', '2017')
my_tesla.motor()
print(my_tesla.get_descriptive_name())
my_new_car = Car('Benz', 'E300L', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading=12
my_new_car.read_odometer()
