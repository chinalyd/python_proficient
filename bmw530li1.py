class Car():
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' +self.manufacturer + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This is a new car, and the current reading range is: " + str(self.odometer_reading) + "KM!")
class Bmw(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.Motor = Motor()
class Motor(Bmw):
    def __init__(self, Motor_size = 60):
        self.Motor_size = Motor_size
    def describe_motor(self):
        print('The engine parameter of this car is: '+ str(self.Motor_size) + ' 6 cylinders, 3.0T turbo, 225kw')
my_tesla = Bmw('BMW', '535Li', '2017')
print(my_tesla.get_descriptive_name())
my_tesla.Motor.describe_motor()
print(my_tesla.model)
